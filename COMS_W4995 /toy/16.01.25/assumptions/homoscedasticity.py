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

X = df['flipper_length_mm']
y = df['body_mass_g']
# %%
model = sm.OLS(y, X).fit()
X = sm.add_constant(df['flipper_length_mm'])
# plt.scatter(model.fittedvalues, model.resid)

# %%
from statsmodels.graphics.gofplots import qqplot
sns.set_style("whitegrid")
qqplot(X,line='s')
plt.show()

# %%
from statsmodels.graphics.gofplots import qqplot
from scipy.stats import norm
errors = np.array([ 0.19686124,  0.35711257, -1.91328024, -0.03582604,  0.76743473,
        1.46564877,  1.56464366,  1.52302986,  0.17136828, -1.72491783,
       -9.86095739,  0.24196227, -0.29900735,  0.82254491, -0.83921752,
       -1.19620662,  0.81252582, -1.10633497,  0.91540212, -0.47917424,
       -1.65177994, -2.6197451 ,  1.35624003, -0.11564828, -1.15099358,
       -0.71984421,  0.51326743,  0.73846658, -1.47852199,  0.54256004,
       -0.29169375, -0.60170661,  0.0675282 , -0.54438272,  0.37569802,
       -0.5297602 ,  0.08704707,  0.31424733, -0.50175704,  0.36163603,
        1.57921282,  0.36139561,  0.34361829, -0.46063877, -1.76304016,
        0.11092259,  0.8219025 , -1.22084365, -1.4123037 , -0.51827022,
       -0.60063869, -0.07201012,  0.97554513, -0.46947439, -0.01349722,
       -0.56228753,  1.05712223, -0.46341769, -0.2257763 , -0.23413696,
       -1.05771093,  0.96864499, -0.23415337,  6.36029532, -1.95967012,
       -1.01283112,  1.47789404,  1.03099952,  1.0035329 ,  1.53803657,
       -0.64511975, -0.70205309,  0.21494605, -0.676922  , -0.39210815,
       -0.90802408,  0.49671415,  0.61167629, -1.98756891, -0.8084936 ,
       -0.32766215, -0.21967189,  0.93128012,  0.64768854, -0.1382643 ,
       -1.32818605, -0.46572975,  0.09707755, -0.30921238, -0.18565898,
       -0.38508228,  0.32875111,  1.85227818,  0.33126343,  0.09176078,
       -1.42474819, -0.3011037 ,  0.32408397,  7.21461167,  0.2088636 ])

errors_percent = errors

plt.figure(figsize=(8, 6))
sns.histplot(errors, kde=True, bins=20)
x = np.linspace(min(errors), max(errors), 1000)
pdf = norm.pdf(x, loc=np.mean(errors), scale=np.std(errors))
plt.plot(x, pdf, color='red', linewidth=2)

plt.grid(True)
plt.show()
errors.max()