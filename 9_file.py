# open file in read mode
with open ("file.txt", "r") as f:
    content = f.read()
    print(content)

# open file in write mode
with open ("file.txt", "w") as f:
    f.write("This is a new line.\n")
    f.write("This is another line.\n")

# open file in append mode
with open ("file.txt", "a") as f:
    f.write("This line will be appended to the file.\n")
    f.write("This is another appended line.\n")

# open file in read and write mode
with open ("file.txt", "r+") as f:
    content = f.read()
    print(content)
    f.write("This line will be added to the end of the file.\n")
    f.write("This is another line added to the end of the file.\n")

with open (r"C:\Users\VIJAY K G\Downloads\employees_500_rows.csv", "r") as f:
    content = f.read()
    print(content)

