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
    df_clean = df.copy()  # to not alter df
    if method == 'drop':
        df_clean = df_clean.dropna(subset=['TotalCharges'])
    elif method == 'impute':
        df_clean['TotalCharges'] = (
            df_clean['TotalCharges'].fillna(df_clean['MonthlyCharges']
                                            * df_clean["tenure"])
        )
    elif method == 'median':
        df_clean['TotalCharges'] = (
            df_clean['TotalCharges'].fillna(df_clean['TotalCharges'].median())
        )
    return df_clean
