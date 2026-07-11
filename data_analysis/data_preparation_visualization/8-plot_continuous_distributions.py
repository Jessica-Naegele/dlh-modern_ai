#!/usr/bin/env python3
"""
function to visualization continuous distributions
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plot_continuous_distributions(df, columns_to_plot=None):
    """Visualizing the distributions of continuous numerical features."""
    if columns_to_plot is None:
        df_plot = df.select_dtypes(include=["number"])
    else:
        df_plot = df[columns_to_plot]

    n_cols = len(df_plot.columns)
    fig, axes = plt.subplots(n_cols, 2, figsize=(10, 3 * n_cols))

    if n_cols == 1:
        axes = axes.reshape(1, -1)

    axes = axes.flatten()

    i = 0
    for col in df_plot.columns:
        # Crucial step: Drop any hidden missing
        # values to perfectly align density scales
        data = df_plot[col].dropna()

        xmin = data.min()
        xmax = data.max()

        # Left Plot: Histogram
        axes[i].hist(data, bins=30, density=True, alpha=0.7, edgecolor="black")

        # Calculate and plot KDE line cleanly
        kde = stats.gaussian_kde(data)
        x_axis = np.linspace(xmin, xmax, 100)
        axes[i].plot(x_axis, kde(x_axis), color="red", linestyle="--")

        # Titles with expected spaces
        axes[i].set_title(f"{col} Histogram + KDE")

        # Move to Right Plot slot
        i += 1

        # Right Plot: Horizontal Boxplot directly from series data
        axes[i].boxplot(data, vert=False)
        axes[i].set_title(f"{col} Boxplot")

        # Move to next row
        i += 1

    plt.tight_layout()
    plt.savefig("Task_8.png")
    plt.show()
