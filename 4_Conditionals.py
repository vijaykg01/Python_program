## CONDITIONALS

# IF-ELSE STATEMENTS

a = int(input("Enter a age: "))
if a >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


a = int(input("Enter a Experience: "))
if a >= 2:
    print("You are experienced.")
else:
    print("You are not experienced.")


a = (input("Enter a username: "))

if len(a) < 10:
    print("Username is less than 10 characters.")
else:
    print("Username is valid.")



# IF-ELIF-ELSE STATEMENTS

a = int(input("Enter a number: "))
if a >= 18:
    print("you are adult.")
elif a < 0:
    print("The number is negative.")
elif a == 0:
    print("The number is zero not a valid number.")
else:
    print("you are minor.")


marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Excellent")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
else:
    print("Fail")
