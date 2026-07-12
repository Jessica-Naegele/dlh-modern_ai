#!/usr/bin/env python3
"""function visualizing churn rates per category"""
import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """visualizing churn rates per category"""

    # change the Churn values from Yes = 1 & No = 0
    df_copy = df.copy()
    # df_copy['Churn'] = df_copy['Churn'].replace({'Yes': 1, 'No': 0})

    # Group by category, get % of Yes and No within each group
    churn_rate = df.groupby(col)['Churn'].value_counts(normalize=True)
    # Filter just the data whit yes churn
    churn_rate_yes = churn_rate[:, 'Yes']
    labels = churn_rate_yes.index
    values = churn_rate_yes.values
    # bar chart
    plt.figure(figsize=(12, 8))
    ax = churn_rate_yes.plot.bar(x=labels, y=values, ylabel='Churn Rate')
    ax.set_title(f'Churn Rate by {col}')
    ax.tick_params(axis='x', rotation=45)
    ax.set_xlabel("")

    plt.show()

    return None
