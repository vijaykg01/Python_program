# ==========================
# PYTHON WHILE LOOP CHEAT SHEET
# ==========================

# 1. Simple while loop
i = 1

while i <= 5:
    print(i)
    i += 1

# 2. Print even numbers
i = 2

while i <= 10:
    print(i)
    i += 2

# 3. Print odd numbers
i = 1

while i <= 10:
    print(i)
    i += 2

# 4. Reverse counting
i = 10

while i >= 1:
    print(i)
    i -= 1

# 5. Infinite loop
while True:
    print("Hello")

# 6. break
i = 1

while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1

# 7. continue
i = 0

while i < 10:
    i += 1

    if i == 5:
        continue

    print(i)

# 8. pass
i = 1

while i <= 5:
    pass
    i += 1

# 9. Nested while loop
i = 1

while i <= 3:

    j = 1

    while j <= 3:
        print(i, j)
        j += 1

    i += 1

# 10. Multiplication table
num = 5
i = 1

while i <= 10:
    print(num * i)
    i += 1

# 11. Sum of numbers
i = 1
total = 0

while i <= 10:
    total += i
    i += 1

print(total)

# 12. Factorial
num = 5
fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print(fact)

# 13. Loop through a string
name = "Python"
i = 0

while i < len(name):
    print(name[i])
    i += 1

# 14. Loop through a list
numbers = [10, 20, 30]
i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1

# 15. Password check
password = "python123"
attempts = 3

while attempts > 0:
    user_password = input("Enter Password: ")

    if user_password == password:
        print("Login Successful")
        break
    else:
        attempts -= 1
        print("Wrong Password")
        print("Attempts Left:", attempts)

if attempts == 0:
    print("Account Locked")


# ==========================
# QUICK NOTES
# ==========================

# while
# Runs until the condition becomes False.

# break
# Exit the loop immediately.

# continue
# Skip the current iteration.

# pass
# Placeholder; does nothing.

# Nested while
# A while loop inside another while loop.