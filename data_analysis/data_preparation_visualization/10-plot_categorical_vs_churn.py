#!/usr/bin/env python3
"""function visualizing churn rates per category"""
import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """visualizing churn rates per category"""

    # change the Churn values from Yes = 1 & No = 0
    df_copy = df.copy()
    df_copy['Churn'] = df_copy['Churn'].replace({'Yes': 1, 'No': 0})

    # how many % said Churn = Yes based on different categories
    values = df_copy.groupby(col)['Churn'].agg('mean').to_list()
    labels = df_copy.groupby(col)['Churn'].agg('mean').index.to_list()

    df_group = df_copy.groupby(col)['Churn'].mean()

    # bar chart
    plt.figure(figsize=(12, 8))
    ax = df_group.plot.bar(x=labels, y=values, ylabel='Churn Rate')
    ax.set_title(f'Churn Rate by {col}')
    ax.tick_params(axis='x', rotation=45)
    ax.set_xlabel("")

    plt.show()

    return None
