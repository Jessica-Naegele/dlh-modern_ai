#!/usr/bin/env python3
"""
Creating a function visualizing correlations between continuous
numeric features
"""
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """
    Function visualizing correlations between continuous numeric features
    df: pandas DataFrame
    Computes pairwise correlations
    Generates an annotated heatmap with coolwarm colormap
    Set vmin = -1 and vmax = 1 so that the heatmap color
    mapping reflects the full correlation range
    Displays the plot
    Returns: None
    """
    plt.figure(figsize=(6, 5))

    # only continuous numeric features
    df_plot = df.select_dtypes(include=['number'])
    # needs pairwise correlation matrix
    corr_matrix = df_plot.corr()

    # set up the heatmap
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    plt.title("Correlation Matrix")
    # let's plot
    plt.show()
