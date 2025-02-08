#
# %% 
# Import Modules
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# %%
dataset = fetch_openml("credit-g")
# %%
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
# %% 
# ! 1.1 Determine which features are continuous and which are categorical.
# ? ✅
df.info() 
# %%
# ! 1.2 Visualize the univariate distribution of each continuous feature, and the distribution of the target.
lst = df.select_dtypes(include=['float64']).columns.tolist()

fig, axs = plt.subplots(2, 2)

axs[0, 0].hist(df[lst[0]]) 
axs[0, 0].set_title(lst[0])

axs[0, 1].hist(df[lst[1]])
axs[0, 1].set_title(lst[1])

axs[1, 0].hist(df[lst[2]])
axs[1, 0].set_title(lst[2])

axs[1, 1].hist(df[lst[4]])
axs[1, 1].set_title(df[lst[4]])




# %%
# ! 1.3 Split data into training and test set. Do not use the test set until a final evaluation in 1.5. Preprocess the data (such as treatment of categorical variables) without using a pipeline and evaluate an initial LogisticRegression model with an training/validation split.
# %%
# ! 1.4 Use ColumnTransformer and pipeline to encode categorical variables (your choice of OneHotEncoder or another one from the categorical_encoder package, or both). Evaluate Logistic Regression, linear support vector machines and nearest neighbors using cross-validation. How different are the results? How does scaling the continuous features with StandardScaler influence the results?
# %%
# ! 1.5 Tune the parameters using GridSearchCV. Do the results improve? Evaluate only the be model on the test set. Visualize the performance as function of the parameters for all three models.
# %%
# ! 1.6 Change the cross-validation strategy from ‘stratified k-fold’ to ‘kfold’ with shuffling. Do the parameters that are found change? Do they change if you change the random seed of the shuffling? Or if you change the random state of the split into training and test data?
# %%
# ! 1.7 Visualize the 20 most important coefficients for LogisticRegression and Linear Support Vector Machines using hyper-parameters that performed well in the grid-search.
