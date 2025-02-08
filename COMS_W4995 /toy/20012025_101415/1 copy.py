# 
# %%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
# %%
df = pd.read_csv('/Users/drozd/VSCODE/courses/COMS_W4995 /modules/2. visualization/data/df.csv')
X = pd.get_dummies(df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'species', 'island', 'sex', 'year']], drop_first=True) # One-hot encoding for categorical
X = X.dropna()
# %%
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)
y = df['body_mass_g'].loc[X.index]
# %%
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=45
)
# %%
n_components = 2
LR = LinearRegression()
LR.fit(X_train, y_train)
# %%
y_pred = LR.predict(X_test)
# %% 
r2_score = r2_score(y_test, y_pred)
# %%
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Actual Body Mass (g)')
plt.ylabel('Predicted Body Mass (g)')
plt.title('LinearRegression Regression: Actual vs Predicted Body Mass')
# %%
r2_score