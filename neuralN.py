# Import libraries.
import tensorflow.keras as kr
import pandas as pd
import numpy as np
import tensorflowjs as tfjs
pp = pd.read_csv("powerprod.csv")

# Import data for modelling (speed greater than 3 m/s & power not equal to 0)
data = pp[(pp["speed"] > 3) & (pp["power"]!=0)]

x = data.iloc[:,:-1].to_numpy()
y = data['power'].to_numpy()
# x = x.reshape(-1, 1)

# Create a new neural network.
m = kr.models.Sequential()
         
# Add multiple layers, initialised with weight and bias.
m.add(kr.layers.Dense(66, input_dim=1, activation="relu",kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
m.add(kr.layers.Dense(32, activation='sigmoid'))
m.add(kr.layers.Dense(16, activation='sigmoid'))
m.add(kr.layers.Dense(1, activation=None))

# Compile the model.
m.compile(loss="mean_squared_error", optimizer="adam")

# fit the keras model on the dataset
m.fit(x, y, epochs=500, batch_size=12)

# Save model output for use in the calculator
m.save('model.h5')

# prediction = m.predict([20])
# print(prediction)