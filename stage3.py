from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib as plt
from matplotlib import *
import numpy as np
import matplotlib.pyplot as plt

# Read the data from a CSV file
data = pd.read_csv('House_Price.csv')

# Create the dependent variable (y) and independent variable (X)
y = data[['Sq.ft']]
X = data[['Price']]

# Fit the linear regression model
model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)
plt.scatter(X,y,color = 'red')

plt.plot(X,model.predict(X),color = "black")

plt.title("Linear Regression")
plt.xlabel("Price")
plt.ylabel("Sq.ft")
plt.show()