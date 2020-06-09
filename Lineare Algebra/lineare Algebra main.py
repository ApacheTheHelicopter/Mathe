import numpy as np
import matplotlib.pyplot as plt
from sympy import Eq, solve, symbols


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

#Vektor 3 declaren, damit er gecallt werden kann

Vektor3 = 0

print("Choose two matrices. Default value is 1 ")

print("First matrice: ")

Vektor1 = np.array([])
n = input("Enter the dimensions you want:  ")

n.isdigit()

if (n.isdigit() == True):
    n = int(n)
    print("Ist digit!")
    
    for i in range(n):
        v = input("Element:  ")
        Vektor1 = np.append(Vektor1, float(v))
    print(Vektor1)

    print("")
    print("Now the second matrice: ")

    Vektor2 = np.array([])
    n = input("Enter the dimensions you want:  ")

    n.isdigit()

    if (n.isdigit() == True):
        n = int(n)
        print("Ist digit!")

        # Code
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

        def VectorDraw(a, b):
            c = np.subtract(b, a)
            print("Vektor zwischen A und B ist: ")
            return c

        # Ouput: E: x = a + r*(b-a) + s*(c-a)
        # Irgendwie Vektor 3 mit einbringen
        def makeLayer(a,b,c):
            print("Third matrice to make the Layer: ")

            Vektor3 = np.array([])
            n = input("Enter the dimensions you want:  ")

            n.isdigit()

            if (n.isdigit() == True):
                n = int(n)
                print("Ist digit!")
                
                for i in range(n):
                    v = input("Element:  ")
                    Vektor3 = np.append(Vektor1, float(v))
                print(Vektor3)
 
                print("")
            c = print("E: x = ", a, " + r* ", (VectorSubs(b, a), " + s* ", VectorSubs(c, a)))
            return c

        print()
        print()
        print("Choose what to do with the Vector!")
        print("You can choose from 'add', 'sub', 'mult' and 'div'")
        print("You can also draw a vector between two matrices by using 'makeVector'")

        choose = input()

        if (choose == "add"):
            print(VectorAdd(Vektor1, Vektor2))
        if (choose == "sub"): 
            print(VectorSubs(Vektor1, Vektor2))
        if (choose == "div"): 
            print(VectorDivd(Vektor1, Vektor2))
        if (choose == "mult"): 
            print(VectorMulti(Vektor1, Vektor2))
        if (choose == "makeVector"):
            print(VectorDraw(Vektor1, Vektor2))
        if (choose == "makeLayer"):
            print(makeLayer(Vektor1, Vektor2, Vektor3))
        
    else:
        print("You took the wrong path, buddy. Enter a number next time.")
            
else:
    print("You took the wrong path, buddy. Enter a number next time.")