"""show some cases for which linearity in a dataset breaks down. 
"""
# 
# %%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %%
df = pd.read_csv('/Users/drozd/VSCODE/courses/COMS_W4995 /modules/2. visualization/data/df.csv')
# %% 
fig, axes = plt.subplots(3, 1, figsize=(10,8))
sns.scatterplot(x=df['flipper_length_mm'], y=df['body_mass_g'], ax=axes[0])
sns.scatterplot(x=df['bill_length_mm'], y=df['body_mass_g'], ax=axes[1])
sns.scatterplot(x=df['bill_depth_mm'], y=df['body_mass_g'], ax=axes[2])
plt.tight_layout()
# %%
fig, axes = plt.subplots(2, 1, figsize=(10,8))
sns.residplot(data=df, x="flipper_length_mm", y="body_mass_g", lowess=True, line_kws={'color': 'red'}, ax=axes[0])
sns.residplot(data=df, x="flipper_length_mm", y="bill_length_mm", lowess=True, line_kws={'color': 'red'}, ax=axes[1])
plt.tight_layout()
# %%
from scipy.stats import norm
np.random.seed(42)

x0 = 20 + 2.5 * np.random.randn(100,)

x1 = np.concatenate((x0,)) + 20 + np.random.normal(loc=2, scale=1)

x2 = np.random.normal(loc=1, scale=1, size=(100,))

# %%
# graph
fig, axis = plt.subplots(3, 2, figsize=(8, 8))
axis[0,0].hist(x0)
axis[0,1].hist(x1)
axis[1,0].hist(x2)
plt.tight_layout()

# %%
# !  theoretically, now as we tune the parameter of std, the higher it goes the less Pearson R there should be
np.corrcoef(x0, x1)

# %%
from statsmodels.graphics.tsaplots import plot_acf
fig, ax = plt.subplots(figsize=(10, 6))
plot_acf(x0, lags=50, ax=ax)

sns.despine(fig=fig, ax=ax)
plt.show()