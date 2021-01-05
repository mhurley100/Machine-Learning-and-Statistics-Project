import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import pandas


pp = pd.read_csv("powerprod.csv")
data = pp[(pp["speed"] > 3) & (pp["power"]!=0)]

x = data.iloc[:,:-1].to_numpy()
y = data['power'].to_numpy()
x = x.reshape(-1, 1)


from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x, y)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
x_poly = poly_reg.fit_transform(x)
poly_reg.fit(x_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)

x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape((len(x_grid), 1))



a = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
print(a)