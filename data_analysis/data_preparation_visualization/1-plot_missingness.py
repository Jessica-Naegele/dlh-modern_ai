#!/usr/bin/env python3
"""
function visualizing missing values in a DataFrame
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """
    df: pandas DataFrame to analyze
    Generates a scatter plot where:
    The x-axis represents row indices (DataFrame records)
    The y-axis represents column names.
    Y-tick labels are explicitly mapped to the DataFrame column names.
    Each missing value is displayed as a vertical bar
    (|), using the default plotting color.
    Displays the plot using Matplotlib
    x Returns: None
    """
    plt.figure(figsize=(12, 8))

    # your code here
    df_nul = df.isnull()
    # print(df_nul)  # helper
    nul = np.where(df_nul)
    # print(nul)  # 'helper'

    x = nul[0]
    y = nul[1]

    plt.scatter(x, y, marker='|')
    # print(df.columns.values)

    plt.title("Missingness Plot")
    plt.yticks(np.arange(0, len(df.columns.values)), df.columns.values)

    plt.tight_layout()
    plt.show()
    return None
