import pandas as pd

cars_reg = pd.read_csv('cars_2025.csv')
fuel_consumption = pd.read_csv('fuelConsumption.csv')

# Normalize the attributes of "fuel_consumption" and "cars_reg" for model and maker
cars_reg['model_normalize'] = cars_reg['model'].str.lower().str.strip()
cars_reg['maker_normalize'] = cars_reg['maker'].str.lower().str.strip()

fuel_consumption['MODEL_normalize'] = fuel_consumption['MODEL'].str.lower().str.strip()
fuel_consumption['MAKE_normalize'] = fuel_consumption['MAKE'].str.lower().str.strip()

# Normalize the 'FUEL' and 'FUELTYPE' columns in fuel_consumption and cars_reg
hybrid_fuel_mapping = {
    'X': 'hybrid_petrol',
    'Z': 'hybrid_petrol',
    'D': 'diesel',
    'E': 'ethanol'
}

normal_fuel_mapping = {
    'X': 'petrol',
    'Z': 'petrol',
    'D': 'diesel',
    'E': 'ethanol'
}

is_hybrid = fuel_consumption['MODEL'].str.contains('hybrid', case=False)

fuel_consumption['fuel_normalize'] = fuel_consumption['FUELTYPE'].map(normal_fuel_mapping)
fuel_consumption.loc[is_hybrid, 'fuel_normalize'] = fuel_consumption.loc[is_hybrid, 'FUELTYPE'].map(hybrid_fuel_mapping)

cars_reg['fuelNorm'] = cars_reg['fuel'].str.lower().str.strip()
fuel_consumption['fuel_normalize'] = fuel_consumption['fuel_normalize'].str.lower().str.strip()

# Merge the datasets on normalized model and maker
merged_datasets = pd.merge(cars_reg, fuel_consumption, 
                     left_on=['model_normalize', 'maker_normalize', 'fuelNorm'], 
                     right_on=['MODEL_normalize', 'MAKE_normalize', 'fuel_normalize'], 
                     how='left')

# Find the matching records where CO2 emissions are not null
total_cars = len(cars_reg)
total_matched = merged_datasets['CO2EMISSIONS'].notnull().sum()

matching_records = merged_datasets[merged_datasets['CO2EMISSIONS'].notnull()]

print("Total records: ", total_cars)
print("Total matched records: ", total_matched)

#Check and handle for missing values and duplicates
print(matching_records.isnull().sum()) # No missing values
print(matching_records.duplicated().sum())

matching_records = matching_records.drop_duplicates()

# Add new columns for CO2 emissions per fuel consumption
matching_records['TotalFuelConsumption'] = matching_records['FUELCONSUMPTION_COMB'] + matching_records['FUELCONSUMPTION_CITY'] + matching_records['FUELCONSUMPTION_HWY'] + matching_records['FUELCONSUMPTION_COMB_MPG']
matching_records['CO2PerLitre'] = matching_records['CO2EMISSIONS'] / matching_records['TotalFuelConsumption']

# Drop unnecessary columns
matching_records = matching_records.drop(columns=['date_reg', 'colour', 'state', 'TRANSMISSION', 'ENGINESIZE', 'CYLINDERS', 'maker', 'model', 'fuel', 'MAKE', 'MODEL', 'FUELTYPE'])

# Rename columns for clarity
matching_records = matching_records.rename(columns={
    'model_normalize': 'Model',
    'maker_normalize': 'Maker',
    'fuelNorm': 'Fuel',
    'fuel_normalize': 'FuelType',
    'FUELCONSUMPTION_COMB': 'FuelConsumption_Combined',
    'FUELCONSUMPTION_CITY': 'FuelConsumption_City',
    'FUELCONSUMPTION_HWY': 'FuelConsumption_Highway',
    'FUELCONSUMPTION_COMB_MPG': 'FuelConsumption_Combined_MPG',
    'Total_fuel_consumption': 'TotalFuelConsumption',
})

# Reorder columns for better readability
matching_records = matching_records[['type', 
                                     'MODELYEAR', 
                                     'VEHICLECLASS', 
                                     'Maker', 
                                     'Model', 
                                     'Fuel', 
                                     'FuelType', 
                                     'FuelConsumption_Combined', 
                                     'FuelConsumption_City', 
                                     'FuelConsumption_Highway', 
                                     'FuelConsumption_Combined_MPG', 
                                     'TotalFuelConsumption', 
                                     'CO2EMISSIONS', 
                                     'CO2PerLitre']]

# Save into a new CSV file
matching_records.to_csv('CarsEmissions.csv', index=False)
print("Merging Completed!")

