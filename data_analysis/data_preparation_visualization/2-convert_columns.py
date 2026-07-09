#!/usr/bin/env python3
"""function which performs type converstion"""

import pandas as pd


def convert_columns(df):
    """
    df: pandas DataFrame containing the columns TotalCharges and SeniorCitizen
    Converts the TotalCharges column to numeric.
    Non-numeric entries should be converted to NaN
    Maps the numeric values in the SeniorCitizen column
    (0 and 1) to categorical strings "No" and "Yes" respectively
    Returns: The modified DataFrame
    """
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['SeniorCitizen'] = df['SeniorCitizen'].replace({0: 'No', 1: 'Yes'})
    return df
