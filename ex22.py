#In this exercise i would like to review what I have learned so far.
#This include, printing, opening a file, defining a function, passing variables from command line.

from sys import argv

script, first, second = argv

value1 = int(argv[1])
value2 = int(argv[2])

#printing
print("HelloWorld")
h = "hello"
w = "World"
print(f"{h}{w}")

#opening a file
file2 = open("file2.txt")

print(file2.read())

def addition(a, b):
    print(f"adding {a} + {b}")
    return a + b

def multiply(a, b):
    return a * b



a = 10
b = 10

c = addition(10, 10)
print("results = ", c)
e = multiply(value1, value2)
print("Multiplication results = ", e)
