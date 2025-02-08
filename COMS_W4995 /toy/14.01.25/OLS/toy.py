# %%
# Import Libaries
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
# %%
# 👍
# Perfect Linear Relationship
X = np.linspace(0, 10, 100)
y = 2*X+1+np.random.normal(0,0.5,100)
sns.scatterplot(x=X,y=y)
z = np.polyfit(X.flatten(), y, 1)
p = np.poly1d(z)
plt.plot(X, p(X), "r--", alpha=0.8)
plt.grid(True, alpha=0.3)
plt.show()
# %%
# 👍
# Two correlated predictors
X1 = np.random.normal(0, 1, 100)
X2 = X1 + np.random.normal(10, 1, 100)  # Correlated with X1
y = 2*X1 + 3*X2 + np.random.normal(0, 0.5, 100)
sns.scatterplot(x=X1, y=y, hue=X2)
z = np.polyfit(X1.flatten(), y, 1)
p = np.poly1d(z)
plt.plot(X1, p(X1) , "r--", alpha=0.8)
plt.grid(True, alpha=0.3)
plt.show()
# %%
# 👎
# Quadratic relationship
X = np.linspace(-5, 5, 100)
y = X**2 + np.random.normal(0, 1, 100)
sns.scatterplot(x=X,y=y)
z = np.polyfit(X.flatten(), y, 1)
p = np.poly1d(z)
plt.plot(X, p(X), "r--", alpha=0.8)
plt.grid(True, alpha=0.3)
plt.show()
# %%
# 👎
# Outlier Sensitivity
X = np.linspace(0, 10, 20)
y = 3 * X + 2
X, y = np.append(X, 5), np.append(y, 0) # outlier
X, y = np.append(X, 8), np.append(y, 50) # outlier
X, y = np.append(X, 10), np.append(y, 50) # outlier
sns.scatterplot(x=X,y=y)
z = np.polyfit(X.flatten(), y, 1)
p = np.poly1d(z)
plt.plot(X, p(X), "r--", alpha=0.8)
plt.grid(True, alpha=0.3)
plt.show()
# %%
# 👎
# Real World Data
from sklearn import datasets
diabetes = datasets.load_diabetes()
X = diabetes.data[:, np.newaxis, 2]  # Single feature
y = diabetes.target
plt.scatter(x=X, y=y)
z = np.polyfit(X.flatten(), y, 1)
p = np.poly1d(z)
plt.plot(X, p(X), "r--", alpha=0.8)
plt.grid(True, alpha=0.3)
plt.show()
# %%
# ! OLS
X1 = sm.add_constant(X1)
model = sm.OLS(y, X1).fit()
plt.hist(model.resid, bins=30, density=True)
print(model.summary())
# %%
# ! Ridge
X1 = sm.add_constant(X1)
penalty = np.array([0] + [1.0] * (X1.shape[1]-1))  # No penalty for intercept
model = sm.OLS(y, X1).fit_regularized(L1_wt=0, alpha=penalty)
print(model.params)
