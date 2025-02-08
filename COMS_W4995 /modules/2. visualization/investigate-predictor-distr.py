# Investigate Predictor Distributions
# %% 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %%
# Visualize Distributions to check if the independants are skewed or symmetric
df = pd.read_csv('data/df.csv')
# %%
x = df['rowid']
hue = df['species']

# %% 
fig, axes = plt.subplots(1, 3)
sns.histplot(x=x, y=df['bill_length_mm'], hue=hue, ax=axes[0])
sns.histplot(x=x, y=df['flipper_length_mm'],hue=hue, ax=axes[1])
sns.histplot(x=x, y=df['body_mass_g'], hue=hue, ax=axes[2])
plt.tight_layout()

# %%
fig, axes = plt.subplots(1, 3)
sns.kdeplot(x=x, y=df['bill_length_mm'], hue=hue, ax=axes[0], fill=True)
sns.kdeplot(x=x, y=df['flipper_length_mm'],hue=hue, ax=axes[1])
sns.kdeplot(x=x, y=df['body_mass_g'], hue=hue, ax=axes[2])
plt.tight_layout()
