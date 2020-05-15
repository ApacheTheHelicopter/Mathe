print("Hello World!");


FirstNumber = 2;
SecondNumber = 2; 

print(FirstNumber+SecondNumber);

if (FirstNumber==1):
    print("First Number is 1!");
else:
    print("First Number is not 1!");

#Name program and Input test
print("Enter your name: ");
nameinput = input()
print("Hello, " + nameinput + ". Now tell me your age, please: ");

#Age program and input
age = float(input())

#True=adult; False=minor
ageCheck = age >= 18;

if (ageCheck == True):
    ageref = "an Adult";
else:
    ageref = "a minor";

print("Oh, so you´re " + ageref);

# greater or smaller
print();
print("Please specify two numbers to check: ")
e = str(float(input()))
print("and: ")
f = str(float(input()))


if e < f:
    print(e + " is less than " + f)
elif e == f:
    print(e + " is equal to " + f)
else:
    print(e + " is greater than " + f)

print()
print()

# Now, glory behold: A probably dumb calculator

print("Define two numbers: ")
g = float(input())
h = float(input())

print()

print("Define what you want to do: ")
print("(Choose from: add and substract)")

define = input()

if (define == "add"):
    print(g + h)
else:
    print(g - h)

# functions

def function1 ():
    print("This is inside a function")
    print("I wonder what cool things I can do with this")

# end of function 1

def function2 ():
    print("This is the second function.")
    print("Notice, how you called this one instead of the other function. What does this say about you?")

print("Please input either function 1 or function 2");
call1 = input()

if (call1 == "function 1"):
    print(function1())
else:
    print(function2())

    #Mehr function tests
    