import tensorflow as tf
from tensorflow import keras

#neuron code
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

#loss calc
model.compile(optimizer='sgd', loss='mean_squared_error')

#data
xs=[1, 2, 3, 4, 5, 6]
ys=[2, 4, 6, 8, 10, 12]

#Train (Epochs gibts Durchläufe an)
model.fit(xs, ys, epochs=1000)

#Estimate what happens at '7'

print(model.predict([7]))