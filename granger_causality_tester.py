import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests

class GrangerCausalityTester:
    def __init__(self, data: pd.DataFrame, dependent_var: str, independent_var: str):
        """
        Initialize the GrangerCausalityTester with the data and variable names.

        :param data: DataFrame containing the time series data
        :param dependent_var: Name of the dependent variable column
        :param independent_var: Name of the independent variable column
        """
        self.data = data
        self.dependent_var = dependent_var
        self.independent_var = independent_var

    def _make_stationary(self, series: pd.Series) -> pd.Series:
        """
        Make a time series stationary by differencing.

        :param series: Time series to make stationary
        :return: Differenced time series
        """
        return series.diff().dropna()

    def test_causality(self, maxlag: int = 2, verbose: bool = False) -> None:
        """
        Perform the Granger causality test between the dependent and independent variables.

        :param maxlag: Maximum lag to consider
        :param verbose: Whether to print the results
        """
        # Make the series stationary
        dependent_stationary = self._make_stationary(self.data[self.dependent_var])
        independent_stationary = self._make_stationary(self.data[self.independent_var])

        # Concatenate the stationary series
        stationary_data = pd.concat([dependent_stationary, independent_stationary], axis=1).dropna()

        # Perform the Granger causality test
        result = grangercausalitytests(stationary_data, maxlag=maxlag, verbose=verbose)

        return result


