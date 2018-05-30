import statsmodels.api as sm
import numpy as np
import pandas as pd
from sklearn import datasets

data = datasets.load_boston()
df = pd.DataFrame(data.data, columns=data.feature_names)

