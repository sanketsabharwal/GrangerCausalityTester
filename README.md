# Granger Causality Tester

The `GrangerCausalityTester` class provides an easy-to-use interface for performing Granger causality tests on time series data. It is primarily designed for a colleague to analyze whether certain metrics help in deciding whether a goal has occurred in football matches or not. But! You could utilize it however you think it best fits your needs. At the end it is a time-series analyzer.

## Requirements

- Python 3.8
- pandas
- statsmodels

You can install the required packages using:

```
pip install pandas statsmodels
```

## Usage

### Initialization

Create an instance of the `GrangerCausalityTester` class by providing a pandas DataFrame containing the time series data, along with the names of the dependent and independent variable columns.

```python
from granger_causality_tester import GrangerCausalityTester

tester = GrangerCausalityTester(data=df, dependent_var='goal_occurrence', independent_var='possession_percentage')
```

### Performing the Test

Call the `test_causality` method to perform the Granger causality test. You can specify the maximum lag to consider (`maxlag`) and whether to print the results (`verbose`).

```python
result = tester.test_causality(maxlag=2, verbose=True)
```

### Example Code

```python
import pandas as pd
import numpy as np
from granger_causality_tester import GrangerCausalityTester

# Create a time series for possession percentage (like a sine wave)
np.random.seed(42)
time_series_length = 100
time = np.linspace(0, 10, time_series_length)
possession_percentage = 50 + 10 * np.sin(time)

# Create a time series for goal occurrence (random binary values with some relationship to possession)
goal_occurrence = (possession_percentage > 55).astype(int)  # Goal occurs when possession percentage is above 55
goal_occurrence = goal_occurrence + np.random.randint(0, 2, time_series_length)  # Adding some noise
goal_occurrence = np.clip(goal_occurrence, 0, 1)  # Ensure values are either 0 or 1

# Create a DataFrame
df = pd.DataFrame({
    'possession_percentage': possession_percentage,
    'goal_occurrence': goal_occurrence
})

# Initialize the GrangerCausalityTester
tester = GrangerCausalityTester(data=df, dependent_var='goal_occurrence', independent_var='possession_percentage')

# Perform the Granger causality test
result = tester.test_causality(maxlag=2, verbose=True)

# Check if p-value is less than 0.05 for any lag
for lag, test_result in result.items():
    p_value = test_result[0]['ssr_ftest'][1]
    if p_value < 0.05:
        print(f"The time series is Granger-causing at lag {lag}. p-value: {p_value}")
    else:
        print(f"The time series is NOT Granger-causing at lag {lag}. p-value: {p_value}")
```

### Example Output

```
Granger Causality
number of lags (no zero) 1
ssr based F test:         F=0.7373  , p=0.3927  , df_denom=95, df_num=1
ssr based chi2 test:   chi2=0.7606  , p=0.3831  , df=1
likelihood ratio test: chi2=0.7576  , p=0.3841  , df=1
parameter F test:         F=0.7373  , p=0.3927  , df_denom=95, df_num=1

Granger Causality
number of lags (no zero) 2
ssr based F test:         F=0.9149  , p=0.4042  , df_denom=92, df_num=2
ssr based chi2 test:   chi2=1.9292  , p=0.3811  , df=2
likelihood ratio test: chi2=1.9102  , p=0.3848  , df=2
parameter F test:         F=0.9149  , p=0.4042  , df_denom=92, df_num=2

The time series is NOT Granger-causing at lag 1. p-value: 0.39269117432340117
The time series is NOT Granger-causing at lag 2. p-value: 0.4041843079877827
```


### Interpretation

The Granger causality test will provide test statistics and p-values for each lag considered. A small p-value (e.g., < 0.05) would suggest that the independent variable Granger-causes the dependent variable.

## Data Preparation

Ensure that the data is in the form of a pandas DataFrame with columns representing the dependent and independent variables. The data should be time series, and the GrangerCausalityTester class will handle differencing to achieve stationarity. Please feel free to change the metrics such as lag basis your convenience and dataset. A high-level of experimentation is inevitable when working with Granger Causality.

## Do whatever you want License

You are free to use this code however you want :)
