#!/usr/bin/env python3
"""function engineers new features from dataset"""

import pandas as pd


def create_features(df):
    """function engineering new features from dataset"""

    # 1 Numservices
    # Number of services customer is subscribed to
    target_cols = [
        col for col in df.columns if
        'No internet service' in df[col].values
        ]
    target_cols.append('YNInternet')
    target_cols.append('MultipleLines')
    target_cols.append('InternetService')

    # creating a help row for InternetServices
    df['YNInternet'] = df['InternetService']
    df['YNInternet'] = df['YNInternet'].replace(
        {
            'DSL': 'Yes',
            'Fiber optic': 'Yes'
            }
        )

    # creating NumServices
    df['NumServices'] = df[target_cols].eq('Yes').sum(axis=1)

    # 2 TenureGroup
    # Define the numeric boundary edges of your buckets
    bins = [0, 12, 24, 48, 60, float('inf')]

    # Define the category names matching those buckets
    labels = ['0-12', '13-24', '25-48', '49-60', '60+']
    df['TenureGroup'] = pd.cut(
        df['tenure'], bins=bins, labels=labels,
        include_lowest=False
        )

    # Drop original columns
    df.drop(columns=target_cols, inplace=True)
    df.drop(columns='tenure', inplace=True)

    return df
