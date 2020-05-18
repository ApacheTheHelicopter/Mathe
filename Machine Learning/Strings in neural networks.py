import tensorflow as tf 
from tensorflow import keras
import numpy as np

# neurons
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])


model.compile(optimizer='sgd', loss='mean_squared_error')


# data
FirstStringArray = ["1", "2", "3"]
SecondList = ["1", "2", "3"]


model.fit(FirstStringArray,SecondList, epochs=1000)


print(model.predict(["2"]))