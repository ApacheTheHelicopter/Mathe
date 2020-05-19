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

print("Choose two Vectors. Default value is 1 ")

print("First: ")

Vektor1 = np.array([])
n = int(input("Enter the number of values you want:  "))

for i in range(n):
    v = input("Element:  ")
    Vektor1 = np.append(Vektor1, v)
print(Vektor1)

print("")
print("Now the second vector: ")

Vektor2 = np.array([])
n = int(input("Enter the number of values you want:  "))

for i in range(n):
    v = input("Element:  ")
    Vektor2 = np.append(Vektor2, v)
print(Vektor2)


def VectorAdd(a, b):
    str(c = a + b) 
    return "c"

def VektorSubs(a, b): 
    a = Vektor1
    b = Vektor2
    c = a - b
    return c

def VektorMulti(a, b): 
    a = Vektor1
    b = Vektor2
    c = a * b 
    return c

def VektorDivd(a, b): 
    a = Vektor1
    b = Vektor2
    c = a / b
    return c

print("Choose what to do with the Vector!")
print("You can choose from 'add', 'sub', 'mult' and 'div'")

choose = input()

if (choose == "add"):
    print(VectorAdd(Vektor1, Vektor2))
    