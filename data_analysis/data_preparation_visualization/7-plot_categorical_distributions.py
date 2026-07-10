#!/usr/bin/env python3
"""
creating a dynamic bar plot
"""
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """
    visualizes categorical feature distribution
    """
    # step 1 prepare dataframe
    df_plot = df.copy()

    if columns_to_plot is None:
        df_plot = df_plot.drop(columns=['Churn'], errors='ignore')
        df_plot = df_plot.select_dtypes(include=['object'])
        # only certain dtypes will be selected
    else:
        df_plot = df[columns_to_plot]

    # create list of columns
    total_features = df_plot.shape[1]

    # define grid of all the plots
    n_cols, n_rows = (3, (total_features + 3 - 1) // 3)

    # Initialize the matplotlib subplots grid
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))

    # your code here
    axes = axes.flatten()

    # Loop through columns and plot
    for i, col in enumerate(df_plot.columns):
        # calc frequencies
        counts = df_plot[col].value_counts()
        x = counts.index.tolist()
        y = counts.values
        # Plot directly onto specific subplot axis
        axes[i].bar(x, y)
        axes[i].set_title(col)
        # rotate x-axis labels by 45 degress
        axes[i].tick_params(axis="x", rotation=45)

    # Step 5: Hide any remaining empty subplots at the end of the grid
    for j in range(total_features, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
