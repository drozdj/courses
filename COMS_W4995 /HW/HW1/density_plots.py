# %% [markdown]
"""
# Task 1: Density Plots (50 points)

1.1. Plot the longtitude vs latitude several ways within a single figure (each in its own axes)
1. Using the matplotlib defaults.
2. Adjusting alpha and marker size to compensate for overplotting.
3. Using a hexbin plot.
4. Subsampling the dataset. 
<p>
For each but the first one, ensure that all the plotting area is used in a reasonable way and that as much information as possible is conveyed; 
this is somewhat subjective and there is no one right answer. <b>[45pts]</b>
<p>
1.2 In what areas are most of the anomalies (measurements) located? <b>[5pts]</b>
"""

# %% 
# ! Import modules
import matplotlib.pyplot as plt
import pandas as pd

# %%
# !  Plot the longtitude vs latitude several ways within a single figure (each in its own axes)
df = pd.read_csv('data/fire_nrt_V1_96617.csv')

x = df['latitude']
y = df['longitude']

# %% 
# ! Plot 1: Default 
plt.plot(x, y)

# %% 
# ! Plot 2: Modify using two params alpha, marker
plt.scatter(x, y, alpha=0.002, marker='.') 

# %% 
# ! Plot 3: Hexbin plot
# More sophisticated for density visualization
# groups data into hexagonal bins rather than individual points
plt.hexbin(x, y, gridsize=300)

# %% 
# ! Plot 4: Random selection of datapoints
df_ten_percent = df.sample(n=10000)
x, y = df_ten_percent['latitude'], df_ten_percent['longitude']

fig, ax = plt.subplots(2, 4, figsize=(10, 5))
ax[0, 0].hexbin(x, y)
ax[0, 1].hexbin(x, y, gridsize=250)
ax[0, 2].hexbin(x, y, gridsize=750)
ax[0, 3].hexbin(x, y, gridsize=1000)

ax[1, 0].hexbin(x, y, bins='log', gridsize=2500)
ax[1, 1].hexbin(x, y, bins='log', gridsize=1500)
ax[1, 2].hexbin(x, y, bins='log', gridsize=1000)
ax[1, 3].hexbin(x, y, bins='log', gridsize=100)