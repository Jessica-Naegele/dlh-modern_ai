#!/usr/bin/env python3
"""function handling missing vlaues in Total Charges"""


def clean_total_charges(df, method='drop'):
    """
    df: pandas DataFrame with missing values in TotalCharges
    method: Strategy to handle missing values:
    'drop': Remove rows with missing TotalCharges
    'median': Fill with column median
    'impute': Replace with MonthlyCharges * tenure
    Returns the modified DataFrame
    """
    if method == 'drop':
        df = df.dropna(subset=['TotalCharges'])
    elif method == 'impute':
        df['TotalCharges'] = df['TotalCharges'].fillna(df['MonthlyCharges'] * df["tenure"])
    elif method == 'median':
        df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())
    return df
