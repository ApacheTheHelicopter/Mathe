import tensorflow as tf 
from tensorflow import keras

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

model.compile(optimizer='sgd', loss='mean_squared_error')

FirstStringArray = ["A", "B", "C", "D", "E", "F"]
SecondStringArray = [1, 2, 3, 4, 5, 6]

model.fit(FirstStringArray, SecondStringArray, epochs=1000)

print(model.predict(["G"]))