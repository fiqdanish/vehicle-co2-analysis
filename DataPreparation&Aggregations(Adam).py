import pandas as pd

## Data Cleaning, Preparation and Wrangling

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
                     
# Find the matching records where CO2 emissions are not null / eliminating missing values
total_cars = len(cars_reg)
total_matched = merged_datasets['CO2EMISSIONS'].notnull().sum()

matching_records = merged_datasets[merged_datasets['CO2EMISSIONS'].notnull()]

print("Total records: ", total_cars)
print("Total matched records: ", total_matched)

# Check and handle for duplicates
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
# matching_records.to_csv('CarsEmissions.csv', index=False)
# print("Merging Completed!")

## Data Aggregation and Grouping

# Group by 'Maker' and aggregate CO2EMISSIONS
maker_emissions_summary = matching_records.groupby('Maker')['CO2EMISSIONS'].agg(['mean', 'median', 'count']).reset_index()

# Group by 'Maker' and aggregate CO2PerLitre
maker_emissions_per_litre_summary = matching_records.groupby('Maker')['CO2PerLitre'].agg(['mean', 'median', 'count']).reset_index()

# Rename columns for better readability
maker_emissions_summary = maker_emissions_summary.rename(columns={
    'mean': 'Average_CO2_Emissions',
    'median': 'Median_CO2_Emissions',
    'count': 'Model_Count',
})

# Rename columns for better readability
maker_emissions_per_litre_summary = maker_emissions_per_litre_summary.rename(columns={
    'mean': 'Average_CO2_Per_Litre',
    'median': 'Median_CO2_Per_Litre',
    'count': 'Model_Count',
})

# Sort the results to see which makers have the highest average emissions
maker_emissions_summary_sorted = maker_emissions_summary.sort_values(by='Average_CO2_Emissions', ascending=False)
maker_emissions_per_litre_summary_sorted = maker_emissions_per_litre_summary.sort_values(by='Average_CO2_Per_Litre', ascending=False)

print("Summary of CO2 Emissions by Car Maker(Highest Emitters):")
print(maker_emissions_summary_sorted.head(10)) # Display top 10 highest emitters

print("\nSummary of CO2 Emissions by Car Maker (Lowest Emitters):")
print(maker_emissions_summary_sorted.tail(10)) # Display 10 lowest emitters

print("\nSummary of CO2 Emissions per Litre by Car Maker (Highest Emitters):")
print(maker_emissions_per_litre_summary_sorted.head(10)) # Display top 10 highest emitters

print("\nSummary of CO2 Emissions per Litre by Car Maker (Lowest Emitters):")
print(maker_emissions_per_litre_summary_sorted.tail(10)) # Display 10 lowest emitters