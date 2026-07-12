#!/usr/bin/env python3
"""function that performs Welch's ttest"""

from scipy import stats


def ttest_numeric(df):
    """Function performing Welch's ttest
    Computes t-test p-value comparing Churn=Yes vs Churn=No for
    each numeric feature
    The Hypothesis being tested is:
    H₀ (null): The means of the variable are equal in Churn=Yes
    and Churn=No groups
    H₁ (alternative): The means differ significantly
    Returns a dictionary: {feature_name: p_value}
    """
    # only numeric features
    df_select = df.select_dtypes(include=['number']).copy()

    # hypothesisis

    """To perform Welch's t-test in Python using the SciPy library,
     use the scipy.stats.ttest_ind function with the argument
     equal_var=False"""

    ttest = {}

    for column in df_select:
        group1 = df[df['Churn'] == 'Yes'][column].dropna()
        group2 = df[df['Churn'] == 'No'][column].dropna()
        result = stats.ttest_ind(group1, group2, equal_var=False)

        ttest[column] = result.pvalue

    return ttest
