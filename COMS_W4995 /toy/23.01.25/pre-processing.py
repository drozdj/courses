# 
# %% 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot
# %%
df = pd.read_csv('data/raw_20TT_Deidentified.csv')
# %%
df = df.dropna()
df['Power'] = df['Power'].astype(np.int64)
df['Cadence'] = df['Cadence'].astype(np.int64)
df['HR'] = df['HR'].astype(np.int64)
df['Max_HR'] = df['Max_HR'].astype(np.int64)
df['HR_percent_max'] = df['HR_percent_max'].round(1).astype(np.float64)
df['Power_relative_to_PPO'] = df['Power_relative_to_PPO'].round(1).astype(np.float64)