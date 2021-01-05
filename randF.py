# Import libraries
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import csv

from flask import jsonify

pp = pd.read_csv("powerprod.csv")

# Speed > 3 & Power != 0
  # Import data for modelling
data = pp[(pp["speed"] > 3) & (pp["power"]!=0)]

x = data.iloc[:,:-1].to_numpy()
y = data['power'].to_numpy()
x = x.reshape(-1, 1)


class RandomF:
    def randF(x): 
        regressor = RandomForestRegressor(n_estimators = 500, random_state = 2)
        regressor.fit(x,y.ravel())
        x_grid = np.arange(min(x),max(x),0.01)
        x_grid = x_grid.reshape(len(x_grid),1)   
        speed = pd.Series(x).to_json(orient='values')  
        prediction =regressor.predict([[x]])
        prediction = pd.Series(prediction).to_json(orient='values')
        a = pd.Series(prediction).to_json(orient='values')
        console.log
        return {"value": prediction}