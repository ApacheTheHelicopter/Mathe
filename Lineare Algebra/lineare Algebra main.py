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

print("Geben Sie 2 Matrizen an. (Default Value=1) ")

print("Erste Matrize: ")

Vektor1 = np.array([])
n = input("Geben Sie die Dimensionen für die Matrize an:  ")

n.isdigit()

if (n.isdigit() == True):
    n = int(n)
    print("Digit check succesful!")
    
    for i in range(n):
        v = input("Element:  ")
        Vektor1 = np.append(Vektor1, float(v))
    print(Vektor1)

    print("")
    print("Jetzt die zweite Matrix: ")

    Vektor2 = np.array([])
    n = input("Geben Sie die Dimensionen für die Matrize an:  ")

    n.isdigit()

    if (n.isdigit() == True):
        n = int(n)
        print("Digit check successful!")

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

        def QuickSub(a, b):
            z = a-b
            return z
        # 
        def Kreuzprodukt(a, b):
            Vektor4 = np.array([])
            c = a[1]*b[2];
            d = a[2]*b[0];
            e = a[0]*b[1];
            f = a[2]*b[1];
            g = a[0]*b[2]; #Vektor1 und 2 vertauscht?
            h = a[1]*b[0];
            cCalc = c-f;
            Vektor4 = np.append(Vektor4, float(cCalc))
            dCalc = d-g;
            Vektor4 = np.append(Vektor4, float(dCalc))
            eCalc = e-h;
            Vektor4 = np.append(Vektor4, float(eCalc))
            print("Normalenvektor: ")
            return Vektor4

        # Ouput: E: x = a + r*(b-a) + s*(c-a)
        def makeLayer(a,b,c):
            print("Geben Sie eine dritte Matrize an, um eine Ebene zu erstellen: ")

            Vektor3 = np.array([])
            n = input("Dimensionen für die Matrize:  ")

            n.isdigit()

            if (n.isdigit() == True):
                n = int(n)
                print()
                print("Digit check successful")
                print()
                
                for i in range(n):
                    v = input("Element:  ")
                    Vektor3 = np.append(Vektor1, float(v))
                print(Vektor3)
 
                print("")
            c = print("E: x = ", a, " + r * ", VectorSubs(b, a), " + s * ", VectorSubs(c, a))
            print()
            return c

        print()
        print()
        print("Was möchten Sie mit den Matrizen machen")
        print("Auswahlmöglichkeiten: 'add', 'sub', 'mult' and 'div'")
        print("Sie können auch einen Vektor erstellen, mithilfe von: 'makeVector'")
        print("Oder Sie erstellen eine Ebene mithilfe von 'makeLayer'.")
        print("Es geht auch die Erstellung eines Normalenvektors mithilfe von 'Kreuzprodukt'.")
        print("Achten Sie auf Groß- und Kleinschreibung")
        print()

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
        if (choose == "Kreuzprodukt"):
            print((Kreuzprodukt(Vektor1, Vektor2)))
        
    else:
        print("Error: Bitte geben Sie eine Zahl an.")
            
else:
    print("Error: Bitte geben Sie eine Zahl an.")