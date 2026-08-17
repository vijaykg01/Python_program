## VARIABLES

a = 30      # variables = container to store a value
b = "harry" # keywords = reserved words in python
c = 71.22   # identifiers = class/function/variable name
d = True    # boolean = True or False
e = None    # NoneType = represents the absence of a value

# a, b, c, d, e are examples of variables in Python.

## DATA TYPES

print(a + c) # int + float = float
print(type(a)) # <class 'int'>
print(type(b)) # <class 'str'>
print(type(c)) # <class 'float'>
print(type(d)) # <class 'bool'>
print(type(e)) # <class 'NoneType'>

## INPUT FUNCTION

a = input("enter name : ") # input() function takes input from user and returns it as a string
print("name is : " + a) 

a = int(input("enter a number : "))
a = float(input("enter a number : "))
a = bool(input("enter a boolean value : ")) 


# find average of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

average = (num1 + num2) / 2

print("The average is:", average)

# Input a number from the user
num = float(input("Enter a number: "))

square = num ** 2

print("The square is:", square)

