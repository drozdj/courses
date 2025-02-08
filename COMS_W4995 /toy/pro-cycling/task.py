# Perform a simple train/test split using scikit-learn.
# %% 
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
# %% 
iris = datasets.load_iris()
# %%
# print(iris.keys())
# print(iris.DESCR)
X, y = iris.data, iris.target
# %% 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# %%
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# %% 
# ! Replicate what StandardScaler() from sklearn does from scratch
# ? why is it important to take the mean (and std) of the columns (4,), rather than entire dataset?

u = np.mean(X_train, axis=0)
s = np.std(X_train, axis=0)
x = X_train

z = (x - u) / s
# %%
# Confirm that re-implementation is correct
(z == X_train_scaled).all()

# %%
X_train.shape
# %% 
# ? why has scaling not transformed to -1 -> 1 
# Min-Max does this strictly. 
# StandardScalar however, only normalizes based on mean and std

plt.figure(figsize=(8, 6))
# Plot original data
plt.scatter(range(len(X_train)), X_train[:, 3], color='blue', label='Original Data', alpha=0.7)
# Plot scaled data
plt.scatter(range(len(z)), z[:, 3], color='red', label='Scaled Data', alpha=0.7)
# Add titles, labels, and legend
plt.title('Original vs Scaled Data')
plt.xlabel('Index')
plt.ylabel('Value')
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)  # Optional: Add a horizontal line at y=0 for reference
plt.legend()

plt.tight_layout()
plt.show()