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



