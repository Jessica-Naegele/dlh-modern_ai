#!/usr/bin/env python3
"""creating a function to remove duplicate rows"""


def remove_duplicates(df):
    """Function removing duplicate rows"""
    df_cleaned = df.drop_duplicates()
    return df_cleaned
