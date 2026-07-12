#!/usr/bin/env python3

import pandas as pd
ttest_numeric = __import__('13-ttest_numeric').ttest_numeric


df = pd.read_csv('precleaned-Telco-Customer-Churn.csv')
print(ttest_numeric(df))

# from scipy import stats

""""
group1 = df[df['Churn'] == 'Yes']['tenure'].dropna()
group2 = df[df['Churn'] == 'No']['tenure'].dropna()

result = stats.ttest_ind(group1, group2, equal_var=False)


print(result)
"""
