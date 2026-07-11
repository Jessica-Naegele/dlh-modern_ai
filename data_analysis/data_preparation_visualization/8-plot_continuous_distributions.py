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
        df_plot = df.select_dtypes(include=["number"]).columns.tolist()
    else:
        df_plot = columns_to_plot

    n_cols = len(df_plot)
    fig, axes = plt.subplots(n_cols, 2, figsize=(10, 3 * n_cols))

    if n_cols == 1:
        axes = axes.reshape(1, -1)

    i = 0
    for i, col in enumerate(df_plot):
        # Crucial step: Drop any hidden missing
        # values to perfectly align density scales
        data = df[col].dropna()

        # Left Plot: Histogram
        axes[i, 0].hist(data, bins=30, density=True, alpha=0.7,
                        edgecolor="black")

        # Calculate and plot KDE line cleanly
        kde = stats.gaussian_kde(data)
        x_range = np.linspace(data.min(), data.max(), 200)
        # evenly spaced curve model by 200
        # x_axis = np.linspace(xmin, xmax, 100)
        axes[i, 0].plot(x_range, kde(x_range), color="red", linestyle="--")

        # Titles with expected spaces
        axes[i, 0].set_title(f"{col} Histogram + KDE")

        # Right Plot: Horizontal Boxplot directly from series data
        axes[i, 1].boxplot(data, vert=False)
        axes[i, 1].set_title(f"{col} Boxplot")

    plt.tight_layout()
    plt.savefig("Task_8.png")
    plt.show()
