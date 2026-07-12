#!/usr/bin/env python3
"""function comparing continiuous features against Churn"""
import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """function comparing continuious numeric feature distributions by churn
    df : DataFrame with Churn
    col: numeric column name
    """
    """version 1    # 1. Group, count into 30 bins, and flatten
    churn_rate = df.groupby('Churn')[col].value_counts(sort=False, bins=30)
    churn_rate_un = churn_rate.reset_index()

    # Pivot it with No and Yes as columns
    churn_piv = churn_rate_un.pivot(index=col, columns='Churn', values='count')

    """

    # version 2
    col_no = df[df['Churn'] == 'No'][col]
    col_yes = df[df['Churn'] == 'Yes'][col]

    # using a figure size (12, 8)
    plt.figure(figsize=(12, 8))

    # plotting with the pivot
    plt.hist([col_no, col_yes], bins=30, label=['No', 'Yes'])

    # add titles and labels
    plt.title(f'{col} Distribution by Churn')
    plt.xlabel(col)
    # plt.ylabel("Count")
    plt.legend(title='Churn')

    plt.show()
