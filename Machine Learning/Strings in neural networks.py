import tensorflow as tf 
from tensorflow import keras

# neurons
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])


model.compile(optimizer='sgd', loss='mean_squared_error')


# data
FirstStringArray = [1, 2, 3, 7, 10, 20, 21]
SecondList = [1, 2, 3, 7, 10, 20, 21]


model.fit(FirstStringArray,SecondList, epochs=1000)


print(model.predict([30]))