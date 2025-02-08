#
# %% Import Modules
import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# %% Read Dataset 
df = pd.read_csv('data/f0ed0af7-d3b9-436a-92b1-a8cdb54c8d24_Data.csv')

# %% Drop first column
# ! Same string 'International tourism, number of arrivals' for all columns
df = df.drop(['Series Name', 'Series Code', 'Country Name', 'Country Name'], axis=1)

# %% Remove NaN
df = df.replace({'..': 0})

# %% Change 'object' values for population to 'int64'
# Get columns from 5th onwards
columns_to_convert = ['2000 [YR2000]', '2001 [YR2001]', '2002 [YR2002]',
       '2003 [YR2003]', '2004 [YR2004]', '2005 [YR2005]', '2006 [YR2006]',
       '2007 [YR2007]', '2008 [YR2008]', '2009 [YR2009]', '2010 [YR2010]',
       '2011 [YR2011]', '2012 [YR2012]', '2013 [YR2013]', '2014 [YR2014]',
       '2015 [YR2015]', '2016 [YR2016]', '2017 [YR2017]', '2018 [YR2018]',
       '2019 [YR2019]']

# Convert to numeric while preserving NaN values
df[columns_to_convert] = df[columns_to_convert].apply(pd.to_numeric, errors='coerce')

# Convert to Int64 (capital I) - this is pandas nullable integer type
df[columns_to_convert] = df[columns_to_convert].round().astype('Int64')


# %%

f