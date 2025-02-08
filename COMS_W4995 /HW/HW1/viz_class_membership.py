# %% [markdown]
"""
# Task 2: Visualizing class membership (50 points)

Visualise the distribution of Brightness temperature I-4 as a histogram (with appropriate settings). Let’s assume we are certain of a fire if the value of temperature I-4 is saturated as visible from the histogram.
<p>
2.1 Do a small multiples plot of whether the brightness is saturated, i.e. do one plot of lat vs long for those points with brightness saturated and a separate for those who are not (within the same figure on separate axes). You can pick any of the methods from 1.1 that you find most suitable. Can you spot differences in the distributions? <b>[20 pts]</b>
<p>
2.2 Plot both groups in the same axes with different colors. Try changing the order of plotting the two classes (i.e. draw the saturated first then the non-saturated or the other way around).
Make sure to include a legend. How does that impact the result? <b>[20 pts]</b>
<p>
2.3 Can you find a better way to compare the two distributions? <b>[10pts]</b>
"""

# %% 
# ! Import modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# %%
# !  Plot the longtitude vs latitude several ways within a single figure (each in its own axes)
df = pd.read_csv('data/fire_nrt_V1_96617.csv')

x = df['latitude']
y = df['longitude']
# %%
fig, ax = plt.subplots(2, 2, figsize=(10, 5))

# Identify saturation point
ax[0,0].hist(df['bright_ti4'], bins=250)
ax[0,0].set_xticks(np.arange(350,370,2))
ax[0,0].set_xlim(350,370)
plt.show()

# %%
df_capped_high_sat = df.loc[df['bright_ti4'] == 367]
df_low_sat = df.loc[df['bright_ti4'] < 367]  

# %%
plt.scatter(df_low_sat['longitude'], df_low_sat['latitude'], alpha=0.2, label='Non-saturated', marker=',')
plt.scatter(df_capped_high_sat['longitude'], df_capped_high_sat['latitude'], alpha=0.2, label='Saturated', marker='.') 
# Don't forget your legend!
plt.legend()

# %%

plt.violinplot(dataset=df_capped_high_sat)
