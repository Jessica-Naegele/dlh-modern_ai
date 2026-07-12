#!/usr/bin/env python3
"""function comparing continiuous features against Churn"""
import matplotlib.pyplot as plt
import seaborn as sns


def plot_numeric_vs_churn(df, col):
    """function comparing continuious numeric feature distributions by churn
    df : DataFrame with Churn
    col: numeric column name
    """

    # using a figure size (12, 8)
    plt.figure(figsize=(12, 8))

    sns.histplot(
        data=df, x=col, hue='Churn', bins=30, multiple='dodge', shrink=0.8
    )

    #add titles and labels
    plt.title(f'{col} Distribution by Churn')
    plt.xlabel(col)
    plt.ylabel("Count")

    plt.show()
