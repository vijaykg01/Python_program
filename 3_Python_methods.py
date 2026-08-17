
a = 'harry' # Single quoted string     
b = "harry" # Double quoted string  
c = '''harry'''  # Triple quoted string for multiple lines

## SLICING WITH SKIP VALUE

word = "amazing"
word[1:6:2] # mzn
word[-7:-1] # amazin
word[:7]    # amazing
word[0:]    # amazing
print(word)

## STRING FUNCTIONS

text = "  Hello Python  "

print("Length:", len(text))
print("Lower:", text.lower())
print("Upper:", text.upper())
print("Title:", text.title())
print("Strip:", text.strip())
print("Capitalize:", text.capitalize())
print("Replace:", text.replace("Python", "World"))
print("Find:", text.find("Python"))
print("Count:", text.count("o"))
print("Starts with Hello:", text.strip().startswith("Hello"))
print("Ends with Python:", text.strip().endswith("Python"))

## list of string methods

# Create a list
numbers = [10, 20, 30]


# append()
numbers.append(40)
print("append():", numbers)

# insert()
numbers.insert(1, 15)
print("insert():", numbers)

# extend()
numbers.extend([50, 60])
print("extend():", numbers)

# remove()
numbers.remove(20)
print("remove():", numbers)

# pop()
numbers.pop(1)
print("pop():", numbers)

# count()
print("count(30):", numbers.count(30))

# index()
print("index(30):", numbers.index(30))

# sort()
numbers.sort()
print("sort():", numbers)

# reverse()
numbers.reverse()
print("reverse():", numbers)

# copy()
new_list = numbers.copy()
print("copy():", new_list)

# clear()
numbers.clear()
print("clear():", numbers)

## TUPLE METHODS

t = (10, 20, 30, 20, 40)

print(t.count(20))
print(t.index(30))

## DICTIONARY METHODS

student = {"name": "Vijay", "age": 21, "course": "Python"}

print("get():", student.get("name"))
print("keys():", student.keys())
print("values():", student.values())
print("items():", student.items())

student.update({"age": 22})
print("update():", student)

student.pop("course")
print("pop():", student)

student.setdefault("city", "Bangalore")
print("setdefault():", student)

new_dict = student.copy()
print("copy():", new_dict)

student.clear()
print("clear():", student)

## SET METHODS

set1 = {10, 20, 30}
set2 = {30, 40, 50}

set1.add(60)
print("add():", set1)

set1.update([70, 80])
print("update():", set1)

print("union():", set1.union(set2))

print("intersection():", set1.intersection(set2))

print("difference():", set1.difference(set2))

print("symmetric_difference():", set1.symmetric_difference(set2))

set1.remove(20)
print("remove():", set1)

set1.discard(100)  # No error
print("discard():", set1)

copy_set = set1.copy()
print("copy():", copy_set)

set1.clear()
print("clear():", set1)

