# 
# %% 
# import libraries
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
# %%
df = pd.read_csv('data/df_encoded.csv')
# %%
# Standardize data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
# %%
pca = PCA(n_components=0.99)
df_pca = pca.fit_transform(df_scaled)
explained_variance = pca.explained_variance_ratio_
# %%
import matplotlib.pyplot as plt
plt.plot(range(1,len(explained_variance) +1),
         np.cumsum(explained_variance))
plt.xlabel('Number of Components')
plt.ylabel('Cumlative Explained Variance Ratio')
plt.show()
# %%
# Get component loadings
loadings = pd.DataFrame(
    pca.components_.T,
    columns=[f'PC{i}' for i in range(1, pca.n_components_ + 1)],
    index=df.columns
)

# %%
loadings