import numpy as np
import matplotlib.pyplot as plt


"""
# Vector build 
x = np.linspace(4, 2, 3)




# Vektoren aus Punkte erstellen

def makeVector(a, b):
    c = b-c
    return c



# plot

N = 3
y = np.zeros(N)
x1 = np.linspace(0, 10, N, endpoint=True)
x2 = np.linspace(0, 10, N, endpoint=False)

#plt.plot(x, y, "o")

#plt.show()
"""

# vector add
# wird mit arrays gemacht


# TODO wenn string input nicht abbrechen, sondern neuen input anfordern
print("Choose two Vectors. Default value is 1 ")

print("First: ")

Vektor1 = np.array([])
n = int(input("Enter the dimensions you want:  "))

for i in range(n):
    v = input("Element:  ")
    Vektor1 = np.append(Vektor1, float(v))
print(Vektor1)

print("")
print("Now the second vector: ")

Vektor2 = np.array([])
n = int(input("Enter the dimensions you want:  "))

for i in range(n):
    v = input("Element:  ")
    Vektor2 = np.append(Vektor2, float(v))
print(Vektor2)

def VectorAdd(a, b):
    c = np.add(a,b)
    return c

def VectorSubs(a, b): 
    c = np.subtract(a,b)
    return c

def VectorMulti(a, b): 
    c = np.multiply(a,b)
    return c

# wenn /0 nicht inf, sondern 0 stehen haben oder so.
def VectorDivd(a, b): 
    c = np.divide(a, b)
    return c

print("Choose what to do with the Vector!")
print("You can choose from 'add', 'sub', 'mult' and 'div'")

choose = input()

if (choose == "add"):
    print(VectorAdd(Vektor1, Vektor2))
if (choose == "sub"): 
    print(VectorSubs(Vektor1, Vektor2))
if (choose == "div"): 
    print(VectorDivd(Vektor1, Vektor2))
if (choose == "mult"): 
    print(VectorMulti(Vektor1, Vektor2))
    