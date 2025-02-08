#
# %%
# ! Import Modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %% 
# ! Dataset
df = pd.read_csv('penguins.csv')

# %%
# ! Data Analysis

# TODO: Calculate the total number of missing values per predictor
# print(f"missing values: {len(df['flipper_length_mm']) - df['flipper_length_mm'].notnull().sum()}")
# very inefficient way of doing it so will ask Perplexity how to improve
plt.figure(figsize=(10,6))
sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')

# TODO: Determine the percentage of missing data for each variable 
(df.isnull().sum() / len(df) * 100).apply(lambda x: f"{(x):.1f}%")

# TODO: Identify if missing values occur randomly or follow patterns
temp = df[df['sex'].isnull()]
# they don't have a relationship, rather 8,9,10,11 rows, somebody was slacking on their job.

# TODO: Drop variables with excessive missing data (>50% missing)
df = df.drop([271,3])

# TODO: check if there are duplicates
df = df.drop_duplicates(subset=["species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex","year"])

# %% 
# TODO: Remove any anomalies

# df[df['bill_length_mm'] > 0].shape
df = df[df['flipper_length_mm'].between(170,240) & 
        df['bill_length_mm'].between(30,60) & 
        df['bill_depth_mm'].between(10,25) &
        df['year'].between(2000,2025)
        ]