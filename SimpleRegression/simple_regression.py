import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

data = datasets.load_boston()
df = pd.DataFrame(data.data, columns=data.feature_names)
target = pd.DataFrame(data.target, columns=["MEDV"])

# Obtain the predictor and response

X = df["RM"]
y = target["MEDV"]

# Log transform the predictor

X = np.log10(X)

# Build the model

model = sm.OLS(y, X).fit()

# Extract the fitted values

predictions = model.predict(X)

# Save the model summary and print it

out = model.summary()
print(out)

# Plot the best fit line

plt.plot(X, predictions)
plt.legend()
plt.show()
