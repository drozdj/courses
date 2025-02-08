"""
Resource Supplement for my blog post 
"Don't fight statistics."
""" 
# %%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot
# %%
df = pd.DataFrame(
    columns=['Volume (h/Week)', # Avg. of Year
             'Nutrition', # Poor, Moderate, Good, Exceptional
             'SC', # Sessions Completed (Percent) 
             '# Goals', # f Long Term Goals. ~1 year timeframe
             'YoE', # Years of Cycling Experience 
             'SM usage', # Social Media # None, Frequent, Constant
             'Mindset', # Performance (to outcompete friend) / Self-Mastery
             'Periodization' # Nordic, German, American, etc.
             ]
    )
# %%
df.loc[len(df)] = [9, 'Moderate', 80, '6', '10', 'Frequent', 'Performance', 'American']
# %%
df.loc[len(df)] = [14, 'Poor', 99, '2', '2', 'None', 'Self-Mastery', 'Nordic']
# %%
df.columns
# %%