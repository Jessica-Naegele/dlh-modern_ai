#!/usr/bin/env python3
"""create a function standardizing numeric columns"""

from sklearn import preprocessing


def scale_numeric(df):
    """
    Scales MonthlyCharges and TotalCharges using StandardScaler (mean=0, std=1)
    Returns the modified DataFrame
    """
    