# Imputation methods to find how accurate
"""_summary_
Im curious to see how the removal of individual datapoints (rows) independant variable can be filled in which different imputation methods:
- Mean Imputation 
- Median Imputation
- Mode Imputation

- KNN Imputation
- Multiple Imputation (MICE)
- IterativeImputer

Then, i will visually inspect to see how far of they really were!
"""

# %%
import numpy as np
import pandas as pd
# %%
df = pd.read_csv('data/df_altered.csv')
# %%
# Index rows 11,12,13 have had their body_mass_g removed, fill them in using the imputation methods
# df['body_mass_g'].fillna(df['body_mass_g'].mean(), inplace=True) # 4205.3
# df['body_mass_g'].fillna(df['body_mass_g'].median(), inplace=True) # 4050.0
# from sklearn.impute import KNNImputer k=1 -> k=10 # 4205.3
# from fancyimpute import KNN k=3 # 4205.3
# from fancyimpute import IterativeImputer # 4205.3
# from fancyimpute import SoftImpute # set all to 0. haven't yet investigated why.
