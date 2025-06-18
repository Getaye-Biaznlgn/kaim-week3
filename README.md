# Insurance Data Analysis Project

A comprehensive toolkit for cleaning, analyzing, and performing statistical tests on insurance datasets. This project provides scripts and Jupyter notebooks for data cleaning, exploratory data analysis (EDA), univariate analysis, and hypothesis testing, tailored for insurance data.

## Features
- Data cleaning and preprocessing for insurance datasets
- Exploratory data analysis (EDA) with summary statistics and missing value analysis
- Univariate analysis with visualizations for numeric and categorical features
- Statistical hypothesis testing (t-test, chi-square) for comparing groups
- Example Jupyter notebooks demonstrating the workflow

## Installation

- Python 3.8+ is required.
- Install dependencies (add to `requirements.txt` as needed):

```bash
pip install -r requirements.txt
```

Typical dependencies include:
- pandas
- numpy
- scipy
- matplotlib
- seaborn

## Usage

### Data Preparation
- Place your raw insurance data file (e.g., `insurance_data.txt`) in `data/raw/`.

### Data Analysis Example
```python
import pandas as pd
from insurance_data_analysis import InsuranceDataAnalysis

df = pd.read_csv('data/raw/insurance_data.txt', sep='|')
analysis = InsuranceDataAnalysis(df)
analysis.display_description()
analysis.clean_and_save_data('data/processed/insurance_data_cleaned.csv')
```

### Hypothesis Testing Example
```python
from hypothesis_testing import HypothesisTester
df = pd.read_csv('data/processed/insurance_data_cleaned.csv')
tester = HypothesisTester(df)
result = tester.t_test('Gender', 'TotalClaims', 'Male', 'Female')
print(result)
```

### Univariate Analysis Example
```python
from univariant_analysis import UnivariateAnalysis
ua = UnivariateAnalysis(df)
ua.plot_numeric_distributions(df)
ua.plot_categorical_distributions(df)
```

### Jupyter Notebooks
- See `notebooks/data_analysis.ipynb` and `notebooks/hypothesis.ipynb` for end-to-end examples.

## Project Structure
- `data/` - Raw and processed data files
- `scripts/` - Main analysis and utility scripts
- `notebooks/` - Jupyter notebooks for EDA and hypothesis testing
- `src/` - (for future expansion) core, models, services, and utilities
- `tests/` - Unit and integration tests
- `config/` - Configuration files

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
