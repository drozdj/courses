"""Calculate and interpret the coefficients from an OLS regression model. For instance, determine what the slope of the regression line implies about the relationship between flipper length and body mass.
"""
# 
# %%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %%
df_train = pd.read_csv('/Users/drozd/VSCODE/courses/COMS_W4995 /modules/2. visualization/data/df_train.csv')
df_test = pd.read_csv('/Users/drozd/VSCODE/courses/COMS_W4995 /modules/2. visualization/data/df_test.csv') 
# %%
import statsmodels.api as sm
y_train = df_train['body_mass_g']
X_train = df_train['flipper_length_mm']

y_test = df_test['body_mass_g']
X_test = df_test['flipper_length_mm']

# %%
X_train = sm.add_constant(X_train)
model = sm.OLS(y_train,X_train).fit()
intercept, slope = model.params
# %%
# statsmodels.api.OLS 
plt.title('OLS Regression Line (statsmodels.api.OLS)')
sns.scatterplot(x='flipper_length_mm',y='body_mass_g',data=df_train)
plt.plot(df_train['flipper_length_mm'], model.predict(X_train), color='red')
plt.show()
# %%
df_test = sm.add_constant(X_test)
predictions = model.predict(X_test)