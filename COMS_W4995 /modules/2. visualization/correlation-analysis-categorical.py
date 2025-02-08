"""
Use contingency tables and chi-square tests to find relationships between categorical predictors
"""
# %% 
# import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %%
df = pd.read_csv('data/df.csv')
filtered_df = df[df['species'].isin(['Chinstrap','Gentoo'])]
# %% 
contingency_table = pd.crosstab(filtered_df['species'], filtered_df['island'])
proportions = contingency_table.div(contingency_table.sum(axis=1), axis=0)
# %%
sns.heatmap(contingency_table, annot=True, cmap='viridis', fmt='g')
plt.show()
sns.heatmap(proportions, annot=True, cmap='viridis', fmt='g') 
plt.show()
# %% 
from scipy.stats import chi2_contingency

chi2, p, dof, expected = chi2_contingency(contingency_table)
print(f"Chi-square Statistic: {chi2}")
print(f"p-value: {p}")
print(f"Degrees of Freedom: {dof}")
print("Expected Frequencies:")
print(expected)