""" 
Is 'Power_relative_to_PPO' related to 'Trial'? 
My guess is that athletes perform better in the latter trial because they are more familiar with the course.
""" 
# %%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %%
df = pd.read_csv('data/processed_20TT_Deidentified.csv')
df.dropna(inplace=True)
# %%
df_pivot = df.pivot_table(index="Participant",
                          columns="Trial",
                          values="Power_relative_to_PPO",
                          aggfunc="mean")
df_pivot.columns = ["Trial1", "Trial2"]
df_pivot.dropna(inplace=True)
# %%
plt.scatter(df_pivot["Trial1"],
            df_pivot["Trial2"],
            color='blue')
plt.show()
# %%
corr = df_pivot["Trial1"].corr(df_pivot["Trial2"])
# %%
from scipy.stats import ttest_rel
t_stat, p_value = ttest_rel(df_pivot["Trial1"], 
                            df_pivot["Trial2"])
print(f"t_stat = {round(t_stat, 2)}")
print(f"p_value = {round(p_value, 2)}")
print(f"pearson_r = {round(corr, 2)}")