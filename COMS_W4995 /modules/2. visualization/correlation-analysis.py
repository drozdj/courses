# 
# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# %%
df = pd.read_csv('data/df_changed.csv')
# %% 
# define only the numerical features, as categorical ones require further work (ie onehot-encoding)
numerical_df = df.select_dtypes(include=['number'])
numerical_df = numerical_df.drop(['year'], axis=1)
numerical_df = numerical_df.drop(['rowid'], axis=1)
# %%
# without noise
sns.pairplot(numerical_df)
# %%
# with noise
noise = np.random.normal(0, 0.9, size=len(numerical_df))
numerical_df['bicept_size_mm'] = numerical_df['bicept_size_mm'] + noise
sns.pairplot(numerical_df)