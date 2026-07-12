#!/usr/bin/env python3
"""function visualizing churn rates per category"""
import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """visualizing churn rates per category"""
    # Group by category, get % of Yes and No within each group
    churn_rate = df.groupby(col)['Churn'].value_counts(normalize=True)
    # Filter just the data whit yes churn
    churn_rate_yes = churn_rate[:, 'Yes']
    labels = churn_rate_yes.index
    values = churn_rate_yes.values
    # bar chart
    plt.figure(figsize=(12, 8))
    plt.bar(labels, values)
    plt.ylabel('Churn Rate')
    plt.title(f'Churn Rate by {col}')
    plt.xticks(rotation=45)
    plt.show()
    return None
