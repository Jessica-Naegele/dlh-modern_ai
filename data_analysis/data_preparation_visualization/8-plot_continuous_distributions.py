#!/usr/bin/env python3
"""
function to visualization continuous distributions
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plot_continuous_distributions(df, columns_to_plot=None):
    """
    visualizing the distributions of continuous numerical features
    """
    if columns_to_plot is None:
        df_plot = df.select_dtypes(include=['number'])
    else:
        df_plot = df[columns_to_plot]

    n_cols = len(df_plot.columns)
    fig, axes = plt.subplots(n_cols, 2, figsize=(10, 3*n_cols))

    if n_cols == 1:
        axes = axes.reshape(1, -1)

    # your code here
    axes = axes.flatten()

    # loop through the columns - creating two graphs 1
    # histogram and 1 tenure boxplox
    i = 0
    for col in df_plot.columns:
        # histogram
        """ KDE = Kernel Density Estimate
        Left subplot: Histogram with KDE using the following settings
        bins = 30
        density = True
        alpha = 0.7
        edgecolor = 'black'
        KDE line color should be red
        Title format: "<column_name> Histogram + KDE"
        """
        data = df_plot[col]
        xmin = data.min()
        xmax = data.max()
        axes[i].hist(data, bins=30, density=True, alpha=0.7, edgecolor='black')
        # calculate and plot KDE
        data.plot(
            kind='kde',
            ax=axes[i],
            color='red',
            linestyle='--',
            ind=np.linspace(xmin, xmax, 100)
            )
        # set the boundaries

        axes[i].set_title(f"{col} Histogram + KDE")
        # boxplot
        i += 1
        """
        Title format: "<column_name> Boxplot"
        """
        data = df_plot[col].to_list()
        axes[i].boxplot(data, vert=False)
        axes[i].set_title(f"{col} Boxplot")
        i += 1

    plt.tight_layout()
    plt.savefig("Task_8.png")
    plt.show()
