# Granger Causality Tester

The `GrangerCausalityTester` class provides an easy-to-use interface for performing Granger causality tests on time series data. It is specifically designed to analyze whether certain metrics help in deciding whether a goal has occurred in football matches or not.

## Requirements

- Python 3.6 or higher
- pandas
- statsmodels

You can install the required packages using:

\`\`\`use any terminal that suits you
pip install pandas statsmodels
\`\`\`

## Usage

### Initialization

Create an instance of the `GrangerCausalityTester` class by providing a pandas DataFrame containing the time series data, along with the names of the dependent and independent variable columns.

\`\`\`python
from granger_causality_tester import GrangerCausalityTester

tester = GrangerCausalityTester(data=df, dependent_var='goal_occurrence', independent_var='possession_percentage')
\`\`\`

### Performing the Test

Call the `test_causality` method to perform the Granger causality test. You can specify the maximum lag to consider (`maxlag`) and whether to print the results (`verbose`).

\`\`\`python
tester.test_causality(maxlag=2, verbose=True)
\`\`\`

### Interpretation

The Granger causality test will provide test statistics and p-values for each lag considered. A small p-value (e.g., < 0.05) would suggest that the independent variable Granger-causes the dependent variable.

## Data Preparation

Ensure that the data is in the form of a pandas DataFrame with columns representing the dependent and independent variables. The data should be time series, and the GrangerCausalityTester class will handle differencing to achieve stationarity.

## Example

An example usage of the class is provided in the `granger_causality_tester.py` file.


## Do whatever License

I am using open-source solutions anyway, so you are free to use this code however you want :)
