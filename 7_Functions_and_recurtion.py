# Function definition without arguments
def func1():
    print("Good Morning")

func1() # Function call


# Function definition without arguments
def avg():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    average = (a + b + c) / 3
    print("Average:", average)

avg() # Function call


# Function definition with arguments
def func1(name,age):
    print("Good Morning")
    print("Name:", name)
    print("Age:", age)

func1("Alice", 25) # Function call


# Function definition with default parameters
def func1(name,ending = "Thank you"):
    print("Good Morning")
    print("Name:", name)
    print("Message:", ending)  

# Function call 
func1("Alice", "Have a nice day") # custom argument will be used
func1("Bob") # default parameter will be used

# RECURSION EX

# Factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number : "))
print("Factorial is", factorial(n))

# sum of n natural numbers using recursion
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)

n = int(input("Enter a number : "))
print("Sum is", sum(n))


# greatest of 3 numbers
def greatest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

a = int(input("Enter first number: "))
b = int(input("Enter second number: ")) 
c = int(input("Enter third number: "))

print("Greatest number is", greatest(a,b,c))


# Celsius to Fahrenheit conversion
def c_to_f(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(c_to_f(0))  


# Fahrenheit to Celsius conversion
def f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print(f_to_c(100))
