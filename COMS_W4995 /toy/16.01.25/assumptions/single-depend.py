"""Calculate and interpret the coefficients from an OLS regression model. For instance, determine what the slope of the regression line implies about the relationship between flipper length and body mass.
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
import statsmodels.api as sm
y = df['body_mass_g']
X = df['flipper_length_mm']
# %%
X = sm.add_constant(X)
model = sm.OLS(y,X).fit()
intercept, slope = model.params
# %%
# statsmodels.api.OLS 
plt.title('OLS Regression Line (statsmodels.api.OLS)')
sns.scatterplot(x='flipper_length_mm',y='body_mass_g',data=df)
plt.plot(df['flipper_length_mm'], model.predict(X), color='red')
plt.show()
# %%
# sns.regplot
plt.title('OLS Regression Line (sns.regplot)')
sns.regplot(data=df, x='flipper_length_mm', y='body_mass_g', line_kws={'color':'red'})
plt.show()
# %%
print(model.summary())
new_x = np.array([[200], [201]]).flatten()
predicted_y = intercept + slope * new_x
round(predicted_y[1] - predicted_y[0], 1) == 49.7
