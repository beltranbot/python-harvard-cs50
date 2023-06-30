# get user input
```python
name = input(<string>, ...)
```


# format string
```python
name = "world"
print(f"hello, {name}")
```

# remove whitespace from str
```python
name = name.strip()
```

# capitalize string
```python
name = name.capitalize()
```

# capitalize each word of a string
```python
name = name.title()
```

# split str
```python
name = name.split()
```

# convert str to int
```python
x = int(x)
```

# format float
```python
print(f"result: {z:,}") # 1000 becomes 1,000
```

# for loop
```python
for _ in range(1_000_000):
    print("meow!") 
```

# while loop
```python
i = 0
while i < 3:
    i += 1
    print("meow!") 
```

# using enumerate
```python
for index, student in enumerate(students):
    print(index, student)
```

# length of a list
```python
my_list = [0, 1, 2]
my_list_length = len(python)
```

# try catch
```python

try:
    x = int(input("What's x? "))
except ValueError:
    print("Please input a number.")
else:
    print(f"x is {x}")
```

# exit program prematurely
```python
import sys
sys.exit("bye")
```

# slices
```python
my_list = [0, 1, 2, 3, 4, 5]
# skip first element
my_list[1:] # [1, 2, 3, 4, 5]
# skip first and last element
my_list[1:-1] [1, 2, 3, 4]
```

# testing packages
1. create test folder
2. add empty __init__.py file
3. run tests
```bash
pytest <main_folder>/test
```

# create and write to file
```python
name = input("What's your name? ")

# w - write
# a - append
# r - read
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
```

```python
name = input("What's your name? ")

# w - write
# a - append
# r - read
file = open("names.txt", "w")
file.write(name)
file.close()
```

# read from a file
```python
with open("names.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip()) # remove newline
```

# sort list
```python
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

# reverse sort
names = []
with open("names.txt") as file:
    for line in sorted(file, reverse=True):
        print(f"hello, {line.rstrip()}")

```


# lambda function
```python
# with open("students.csv") as file:
#     for line in file:
#         [name, house] = line.rstrip().split(",")
#         print(f"{name} is in {house}")

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")

```