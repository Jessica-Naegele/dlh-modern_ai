#!/usr/bin/env python3
"""function encoding features"""

import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """
    df: pandas DataFrame
    The function should encode:
    Churn: LabelEncoder (No→0, Yes→1)
    Partner, Dependents, PaperlessBilling, SeniorCitizen: OrdinalEncoder (No→0, Yes→1)
    Contract, PaymentMethod: One-hot encoding with drop first set to True
    TenureGroup: Alphabetical order OrdinalEncoder
    Returns:
    The encoded DataFrame
    The Fitted LabelEncoder for Churn
    The Fitted OrdinalEncoder for binary columns
    The Fitted OrdinalEncoder for TenureGroup
    """
    df_copy = df.copy()

    # Label Encoder: Churn
    le_churn = preprocessing.LabelEncoder()
    df_copy['Churn'] = le_churn.fit_transform(df_copy['Churn'])

    # OrdinalEncoer for binary features
    cols = ['Partner', 'Dependents', 'PaperlessBilling', 'SeniorCitizen']
    oe_binary = preprocessing.OrdinalEncoder(dtype='int64')
    df_copy[cols] = oe_binary.fit_transform(df_copy[cols])

    # sort TenureGroup
    sort_tenure_group = sorted(df_copy['TenureGroup'].unique())

    oe_tenure = preprocessing.OrdinalEncoder(
        categories=[sort_tenure_group],
        dtype='int64')
    df_copy['TenureGroup'] = oe_tenure.fit_transform(df_copy[['TenureGroup']])

    # one-hot encode unordered features 
    one_hot_cols = ['Contract', 'PaymentMethod']
    df_copy = pd.get_dummies(
        df_copy,
        columns=one_hot_cols,
        drop_first=True,
        dtype=int
        )

    return df_copy, le_churn, oe_binary, oe_tenure
