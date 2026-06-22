import pandas as pd 

# Load CarsEmissions dataset

cars_emissions = pd.read_csv('CarsEmissions.csv')

# Find cars with highest CO2 emissions
highest_emissions = cars_emissions[['Maker', 'Model', 'CO2EMISSIONS']].sort_values(by='CO2EMISSIONS', ascending=False).reset_index().head(5)
print("Cars with highest CO2 emissions:")
print(highest_emissions)

#Find cars with lowest CO2 emissions
lowest_emissions = cars_emissions[['Maker', 'Model', 'CO2EMISSIONS']].sort_values(by='CO2EMISSIONS', ascending=True).reset_index().head(5)
print("\nCars with lowest CO2 emissions:")
print(lowest_emissions)
