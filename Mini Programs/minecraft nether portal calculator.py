import numpy as np

print()
print("Type in the Coordinates as follows:")
print("First the x and then the z.")
print("")

target = np.array([])
n = 2

for i in range(n):
    v = input("Coordinates: ")
    target = np.append(target, float(v))
print("")

print("Proceed with ", target, "?")
print("Type Yes or No.")

prompt = input()

def calc(a):
    c = target
    d = c/8
    return d

if (prompt == "Yes"):
    print("The Portal Coordinates in the Nether are (x, z): ", calc(target))
else:
    print("Ok.")

