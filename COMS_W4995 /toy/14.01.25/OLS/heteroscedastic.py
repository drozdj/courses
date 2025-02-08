# %%
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# %%
np.random.seed(42)
# %%
X = np.linspace(1, 100, 500)
# %%
noise = np.random.normal(0, X * 0.5)
Y = 2 * X + noise
plt.scatter(X, Y)
# %%
model = sm.OLS(Y, X).fit()
plt.scatter(model.fittedvalues, model.resid)