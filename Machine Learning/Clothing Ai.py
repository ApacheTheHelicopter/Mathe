# Label defs

# 0 Trouser
# 1 Pullover
# 2 Dress
# 3 Coat
# 4 Sandal
# 5 Shirt
# 6 Sneaker
# 7 Bag
# 8 Ankle Boot


import tensorflow as tf
import numpy as np


mnist = tf.keras.datasets.fashion_mnist
#variablen
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

# 60k training Bilder, 28x28 Pixel, 1=Schwarz/Weiß, z.B. RGB=3
training_images= training_images.reshape(60000, 28, 28, 1)
#normalisieren
training_images = training_images / 255.0
test_images = test_images.reshape(10000, 28, 28, 1)
test_images = test_images / 255.0

model = tf.keras.models.Sequential([
    #Bilder flatten
    tf.keras.layers.Flatten(),
    #Anzahl der Neurons pro Layer
    #relu = Löscht alles unter x=1, danach Linearer Zusammenhang
    tf.keras.layers.Dense(128, activation='relu'),
    #10 Verschiedene Kleidungsstücke, softmax=Wahrscheinlichkeiten 
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compiler argumente 
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# training_images sollen mit training_labels abgeglichen werden
# Ai soll erkennen welche training_images zu welchen training_labels gehören
model.fit(training_images, training_labels, epochs=20)

# test
classes = model.preict(test_images)
predicted_classes = np.argmax(classes, axis=1)
print(classes[0])
print(test_labels[0])

mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

import matplotlib as mpl

mpl.imshow(test_images[0], cmap='Greys_r')


# Eigene Bilder idents

# Bilder import

from keras.preprocessing import image
import cv2 
import matplotlib.pylot as plt 

uploaded = files.upload()

for fn in uploaded.keys():
    # Loop für mehrere Bilder
    path = '/content/' + fn
    img = cv2.imread(path)

    # Bilder formatieren
    img = cv2.resize(img, (28, 28))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    x = image.img_to_array(img)
    x = x / 255.0
    x = np.expand_dims(x, axis=0)
    x = x.reshape(1, 28, 28, 1)

    # calc answer from neural network
    calsses = model.predict(x)
    print(classes[0])
    print(np.argmax(classes[0]))
    plt.imshow(img, cmap='Grays_r')
