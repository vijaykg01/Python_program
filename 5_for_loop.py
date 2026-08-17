# ==========================
# PYTHON FOR LOOP CHEAT SHEET
# ==========================

# 1. Simple for loop
for i in range(5):
    print(i)

# 2. Start and End
for i in range(1, 6):
    print(i)

# 3. Start, End, Step
for i in range(2, 11, 2):
    print(i)

# 4. Reverse Order
for i in range(10, 0, -1):
    print(i)

# 5. Loop through a String
name = "Python"

for ch in name:
    print(ch)

# 6. Loop through a List
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

# 7. Loop through a Tuple
numbers = (10, 20, 30)

for num in numbers:
    print(num)

# 8. Loop through a Set
s = {1, 2, 3}

for item in s:
    print(item)

# 9. Loop through Dictionary Keys
student = {"name": "Vijay", "age": 22}

for key in student:
    print(key)

# 10. Loop through Dictionary Values
for value in student.values():
    print(value)

# 11. Loop through Dictionary Keys and Values
for key, value in student.items():
    print(key, value)

# 12. Using enumerate()
fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# 13. Using zip()
names = ["Ram", "Shyam", "John"]
marks = [90, 85, 95]

for name, mark in zip(names, marks):
    print(name, mark)

# 14. break
for i in range(1, 11):
    if i == 6:
        break
    print(i)

# 15. continue
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# 16. pass
for i in range(5):
    pass

# 17. Nested for loop
for i in range(3):
    for j in range(3):
        print(i, j)

# 18. Multiplication Table
num = 5

for i in range(1, 11):
    print(num * i)

# 19. Sum of Numbers
total = 0

for i in range(1, 11):
    total += i

print(total)

# 20. Factorial
fact = 1

for i in range(1, 6):
    fact *= i

print(fact)