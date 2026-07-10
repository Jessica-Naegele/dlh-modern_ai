#!/usr/bin/env python3
"""function for displaying churn distribution"""

import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """
    function visualizing churn class distribution
    """
    plt.figure(figsize=(12, 8))

    # your code here

    # step 1 aggregation
    val = df['Churn'].value_counts().values  # list with values
    values = df['Churn'].value_counts().index.tolist()  # list with Value Names

    # define colors
    colors = ['skyblue', 'salmon']

    # Step 2 plotting
    plt.bar(values, val, color=colors)

    plt.title('Churn Distribution')
    plt.ylabel('Count')
    plt.show()

    return None
