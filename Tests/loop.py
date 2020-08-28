# Loop test

#List maker

import numpy as np

list = np.array([])

n = input()

for i in range(n):
    v = input("Liste: ")
    target = np.append(target, float(v))

print (v)