# Car CO2 Emissions Analysis

A data analytics project that merges Malaysian car registration data with fuel consumption data to analyze, rank, and cluster cars by their CO2 emissions.

**Course:** SECP 3223 — Data Analytics Programming
**Institution:** Universiti Teknologi Malaysia (UTM)

## Group Members

| No. | Name | Matric Number |
|-----|------|---------------|
| 1 | Muhammad Adam Bin Razali | A23CS0116 |
| 2 | Muhammad Naim Bin Abdullah | A23CS0134 |
| 3 | Muhammad Afiq Danish Bin Mohd Hazni | A23CS0118 |

## Overview

Cars are one of the largest contributors to CO2 emissions. This project takes a large car registration dataset (260,000+ records) and combines it with a fuel consumption dataset to estimate the real-world emissions footprint of cars on the road. The goal is to turn two separate, messy datasets into a single clean source of insight — identifying which makers and models pollute the most, and grouping them into emission tiers.

## Datasets

| File | Description |
|------|-------------|
| `cars_2025.csv` | Car registration records (maker, model, fuel, etc.) |
| `FuelConsumption.csv` | Fuel consumption and CO2 emissions per car model |
| `CarsEmissions.csv` | **Output** — cleaned and merged dataset produced by the pipeline |

## Project Structure

| File | Description |
|------|-------------|
| `DataPreparation.py` | Cleans, normalizes, and merges the two raw datasets into `CarsEmissions.csv` |
| `DataAggregations.py` | Finds cars with the highest and lowest CO2 emissions |
| `DataPreparation&Aggregations(Adam).py` | Combined preparation + aggregation by car maker |
| `Project Report.ipynb` | Full project notebook: preparation, analysis, clustering, and visualizations |
| `Project SECP 3223 2024202502.pdf` | Project specification / brief |

## Methodology

### Phase 1 — Data Preparation and Cleaning
- Normalized text columns (lowercase + strip whitespace) for `maker`, `model`, and `fuel`.
- Mapped fuel codes (`X`, `Z`, `D`, `E`) to readable fuel types, with special handling for hybrid vehicles.
- Merged the datasets with a left join on normalized maker, model, and fuel type.
- Removed missing values and duplicate records, reducing ~263,000 records to ~8,000 matched, clean records.
- Renamed and reordered columns, and set a multi-index on `Maker` and `Model` for easier access.

### Phase 2 — Data Analytics and Visualization
- **Aggregation:** Grouped CO2 emissions by maker and model (mean, median, count) to rank the highest and lowest emitters.
- **Clustering:** Applied **K-Means** clustering on average CO2 emissions, using the **elbow method** to select K = 3 clusters for both makers and models.
- **Visualization:** Bar plots and scatter plots (matplotlib + seaborn) showing emission tiers by cluster.

## Tech Stack

- **Python 3**
- **pandas** — data cleaning, wrangling, and aggregation
- **scikit-learn** — K-Means clustering and feature scaling
- **matplotlib** & **seaborn** — data visualization
- **Jupyter Notebook** — analysis and reporting

## How to Run

1. Install dependencies:
   ```bash
   pip install pandas scikit-learn matplotlib seaborn
Here's a complete `README.md` for your project:

```markdown
# Car CO2 Emissions Analysis

A data analytics project that merges Malaysian car registration data with fuel consumption data to analyze, rank, and cluster cars by their CO2 emissions.

**Course:** SECP 3223 — Data Analytics Programming
**Institution:** Universiti Teknologi Malaysia (UTM)

## Group Members

| No. | Name | Matric Number |
|-----|------|---------------|
| 1 | Muhammad Adam Bin Razali | A23CS0116 |
| 2 | Muhammad Naim Bin Abdullah | A23CS0134 |
| 3 | Muhammad Afiq Danish Bin Mohd Hazni | A23CS0118 |

## Overview

Cars are one of the largest contributors to CO2 emissions. This project takes a large car registration dataset (260,000+ records) and combines it with a fuel consumption dataset to estimate the real-world emissions footprint of cars on the road. The goal is to turn two separate, messy datasets into a single clean source of insight — identifying which makers and models pollute the most, and grouping them into emission tiers.

## Datasets

| File | Description |
|------|-------------|
| `cars_2025.csv` | Car registration records (maker, model, fuel, etc.) |
| `FuelConsumption.csv` | Fuel consumption and CO2 emissions per car model |
| `CarsEmissions.csv` | **Output** — cleaned and merged dataset produced by the pipeline |

## Project Structure

| File | Description |
|------|-------------|
| `DataPreparation.py` | Cleans, normalizes, and merges the two raw datasets into `CarsEmissions.csv` |
| `DataAggregations.py` | Finds cars with the highest and lowest CO2 emissions |
| `DataPreparation&Aggregations(Adam).py` | Combined preparation + aggregation by car maker |
| `Project Report.ipynb` | Full project notebook: preparation, analysis, clustering, and visualizations |
| `Project SECP 3223 2024202502.pdf` | Project specification / brief |

## Methodology

### Phase 1 — Data Preparation and Cleaning
- Normalized text columns (lowercase + strip whitespace) for `maker`, `model`, and `fuel`.
- Mapped fuel codes (`X`, `Z`, `D`, `E`) to readable fuel types, with special handling for hybrid vehicles.
- Merged the datasets with a left join on normalized maker, model, and fuel type.
- Removed missing values and duplicate records, reducing ~263,000 records to ~8,000 matched, clean records.
- Renamed and reordered columns, and set a multi-index on `Maker` and `Model` for easier access.

### Phase 2 — Data Analytics and Visualization
- **Aggregation:** Grouped CO2 emissions by maker and model (mean, median, count) to rank the highest and lowest emitters.
- **Clustering:** Applied **K-Means** clustering on average CO2 emissions, using the **elbow method** to select K = 3 clusters for both makers and models.
- **Visualization:** Bar plots and scatter plots (matplotlib + seaborn) showing emission tiers by cluster.

## Tech Stack

- **Python 3**
- **pandas** — data cleaning, wrangling, and aggregation
- **scikit-learn** — K-Means clustering and feature scaling
- **matplotlib** & **seaborn** — data visualization
- **Jupyter Notebook** — analysis and reporting

## How to Run

1. Install dependencies:
   ```bash
   pip install pandas scikit-learn matplotlib seaborn
   ```

2. Run the data preparation pipeline to generate `CarsEmissions.csv`:
   ```bash
   python DataPreparation.py
   ```

3. Run the aggregation analysis:
   ```bash
   python DataAggregations.py
   ```

4. Or open the full report for the complete analysis and visualizations:
   ```bash
   jupyter notebook "Project Report.ipynb"
   ```

## Key Findings

- Only ~8,000 of 263,578 registration records successfully matched the fuel consumption data, due to inconsistent naming across datasets.
- **Highest-emitting makers** included luxury and performance brands such as Aston Martin, Bentley, Maserati, and Porsche.
- **Lowest-emitting makers** were dominated by Toyota, Honda, Mitsubishi, and Mazda.
- K-Means clustering cleanly separated cars into low, medium, and high emission tiers.
```

Want me to tweak anything — for example, add a license section, screenshots/charts placeholders, or adjust the file names to match exactly what you'll commit?
