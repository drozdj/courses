# %%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %%
df = pd.read_csv('/Users/drozd/VSCODE/courses/COMS_W4995 /modules/2. visualization/data/df.csv')
# %%
X = df['flipper_length_mm']
y = df['body_mass_g']
# %%
sns.scatterplot(x=X,y=y)
z = np.polyfit(X.to_numpy().flatten(), y, 1)
p = np.poly1d(z)
plt.plot(X, p(X) , "r--", alpha=0.8)
plt.grid(True, alpha=0.3)
plt.show()
# %%
import statsmodels.api as sm
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())
# print(model.params)

# %%
X_new = sm.add_constant(np.array((201, 0))) # 200 flipper_length_mm
predictions = model.predict(X_new)
# %%
plt.scatter(model.fittedvalues, model.resid)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
# %%
import statsmodels.stats.diagnostic as sms
X = sm.add_constant(X)
f_stat, p_value, ordering = sms.het_goldfeldquandt(y, X, drop=0.2)
# %%
print(model.rsquared)

