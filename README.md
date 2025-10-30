# Distributions

A Python library for statistical calculations and distribution analysis.

## Description

This project provides a comprehensive `Data` class containing functions to support various statistical calculations, including:

- Normal distributions (PDF, CDF)
- Poisson distributions (PMF, CDF, PPF)
- Binomial distributions
- Exponential probability
- Sample statistics and central tendencies
- Hypothesis testing
- Linear regression
- Confidence intervals and critical values
- Z-scores and T-scores

## Installation

### Prerequisites

- Python 3.x
- pip

### Setup

1. Clone or download this repository
2. Navigate to the project directory
3. Run the setup command:

```bash
make setup
```

This will:
- Create a virtual environment (default: `.venv`)
- Initialize a git repository if one doesn't exist
- Install all required dependencies

### Manual Setup

If you prefer to set up manually:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Dependencies

- numpy
- pandas
- scipy
- statsmodels
- ipython
- scikit-learn

## Usage

```python
from datum import Data

# Create a Data instance
data = Data(N=100, mu=50, sigma=10)

# Generate random data
cnt, min_val, max_val, mu, sigma, x_arr = data.make_data(N=100, mu=50, sigma=10)

# Calculate central tendencies
cnt, mu, sigma, min_val, max_val = data.get_central_tendency(x_arr)

# Generate normal distribution
dist = data.make_normal_pdf(low=-3, upp=3, N=1000)

# Calculate z-scores
z_score = data.convert_to_std_dev(x=55, mu=50, sigma=10)

# Get critical values
critical_value = data.get_z_critical_value(x=0.95)
```

## Makefile Targets

- `make setup` - Initialize project environment
- `make activate` - Activate virtual environment
- `make clean` - Remove build artifacts and cache files

## Features

### Distribution Generation
- Normal distributions (continuous and discrete)
- Poisson distributions
- Binomial distributions

### Statistical Calculations
- Mean, median, mode
- Variance and standard deviation
- Frequencies and central tendencies
- Sample proportions

### Hypothesis Testing
- Z-tests and T-tests
- Chi-square tests
- P-value calculations
- Rejection regions
- Confidence intervals

### Regression Analysis
- Linear regression
- Slope and intercept calculation
- Correlation coefficients
- Predicted values

## Author

S Cotton

## License

This project is available for personal and educational use.
