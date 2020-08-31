# Originalfunktion eingeben

import numpy as np


originalfunktion = np.array([])


# Form des inputs: ax^n + bx^n + cx^n + d

zahlenanzahl = input()

for i in range(zahlenanzahl):
    v = input("Dimensionen: " )
    zahlenanzahl = np.append(zahlenanzahl, v)


# Ableitungen berechen

