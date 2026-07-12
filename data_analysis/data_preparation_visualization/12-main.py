#!/usr/bin/env python3

import pandas as pd
from scipy import stats
chi_square_tests = __import__('12-chi_square_tests').chi_square_tests


df = pd.read_csv('precleaned-Telco-Customer-Churn.csv')

#print(df.columns)
# print(df[["Churn", "gender"]].to_numpy())

print(chi_square_tests(df))

#data = df[["Churn", "gender"]].to_numpy()

"""
contingency = pd.crosstab(df['Churn'], df['gender'])
chi2, p, dof, expected = stats.chi2_contingency(contingency)
chi_square = {"gender": p}

print(f"data: {contingency}")
print(f"p_value: {p}")
print(f"chi_square = {chi_square}")

"""