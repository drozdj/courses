#
# %% 
# Import required rpy2 modules
import rpy2.robjects.packages as rpackages
from rpy2.robjects.vectors import StrVector

# Import R's utility package
utils = rpackages.importr('utils')

# Select CRAN mirror
utils.chooseCRANmirror(ind=1)

# Define packages to install
packages_to_install = ('caret', 'AppliedPredictiveModeling')

# Install packages that aren't already installed
names_to_install = [x for x in packages_to_install if not rpackages.isinstalled(x)]
if len(names_to_install) > 0:
    utils.install_packages(StrVector(names_to_install))
