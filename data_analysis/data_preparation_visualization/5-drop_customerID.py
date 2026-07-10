#!/usr/bin/env python3
"""Function removing customerID"""


def drop_customerID(df):
    """function dropping ID --> as unique identifiers lack predictive value"""
    df_clean = df.drop(columns=['customerID'])
    return df_clean
