#!/usr/bin/env python3
"""function performing chi-square testes"""

import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """
    df: pandas DataFrame with Churn and categorical columns
    Computes the Chi-square p-value to test the independence
    Returns a dictionary: {feature_name: p_value}
    """
    """
    chisqaure: goodness-of-fit
    chi2_contingency: tests of independence
    how ci2_contingency needs its data:
    data = [
    [45, 35, 10],  # Male: Prefer Product A, B, C
    [30, 50, 15]   # Female: Prefer Product A, B, C
    ]
    chi2_stat, p_value, dof, expected = chi2_contingency(data)
    """
    df_sel = df.copy()
    df_sel = df.select_dtypes(include=['object'])
    df_sel = df_sel.drop(columns=['Churn'], errors='ignore')
    colums = df_sel.columns

    chi_square = {}

    for col in df_sel:
        contingency = pd.crosstab(df[col], df['Churn'])
        chi2, p, dof, expected = stats.chi2_contingency(contingency)
        chi_square[col] = p

    return chi_square
