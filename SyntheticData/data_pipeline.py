import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import unittest

data = pd.read_csv('mock_data.csv')
X = data['X']
Y = data['Y']

slope, intercept, r_value, p_value, std_err = linregress(X, Y)

original_m = 2.5
original_b = 5.0

tolerance = 0.2

# Plotting
plt.scatter(X, Y, label='Data', color='blue', alpha=0.5)

# Original line
plt.plot(X, original_m * X + original_b, label='Original Line', color='green', linestyle='dashed')

# Fitted line
plt.plot(X, slope * X + intercept, label='Fitted Line', color='red')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Mock Data Fit')
plt.legend()
plt.grid(True)

plt.show()