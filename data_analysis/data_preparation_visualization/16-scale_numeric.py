#!/usr/bin/env python3
"""create a function standardizing numeric columns"""

from sklearn import preprocessing


def scale_numeric(df):
    """
    Scales MonthlyCharges and TotalCharges using StandardScaler
    (mean=0, std=1)
    Returns the modified DataFrame
    """
    df_copy = df.copy()

    # group target columns
    cols = ['MonthlyCharges', 'TotalCharges']

    # initialize scikit learn scaler object
    scaler = preprocessing.StandardScaler()

    # compute mean/std and transform values all at once
    df_copy[cols] = scaler.fit_transform(df_copy[cols])

    return df_copy
