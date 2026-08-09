# =====================================
# 1. Python Output Basics
# =====================================

# 1: Print the message "Welcome to Python".

print("Welcome to Python")

# Output:
# Welcome to Python


# 2: Perform addition, subtraction, multiplication, and division of two numbers.

a = 10
b = 20

print("add:", a + b)
print("sub:", a - b)
print("mult:", a * b)
print("div:", a / b)

# Output:
# add: 30
# sub: -10
# mult: 200
# div: 0.5


# =====================================
# 2. Variables and Data Types
# =====================================

# 3: Create variables of string, float, integer, and boolean data types.
# Print their data types.

name = "Vishnu"
student_id = 12.0
age = 20
is_learning_python = True

print(type(name))
print(type(student_id))
print(type(age))
print(type(is_learning_python))

# Output:
# <class 'str'>
# <class 'float'>
# <class 'int'>
# <class 'bool'>


# 4: Define a variable and print its value.

a = 10
print(a)

# Output:
# 10


# 5: Assign different values to the same variable and print it each time.

a = 1
print(a)

a = 2
print(a)

# Output:
# 1
# 2


# 6: Assign the value of one variable to another variable and print both.

a = 1
b = 2

a = b

print(a)
print(b)

# Output:
# 2
# 2


# =====================================
# 3. Operators and Expressions
# =====================================

# 7: Evaluate an expression using the order of operations.

print(10 / 2 + 3)

# Output:
# 8.0


# =====================================
# 4. Strings
# =====================================

# 8: Add two strings and print the result.

a = "1" + "2"
print(a)

# Output:
# 12


# 9: Concatenate a greeting with a name.

name = "Vishnu"
print("Hi " + name)

# Output:
# Hi Vishnu


# 10: Create two stars using string addition.

a = "*" + "*"
print(a)

# Output:
# **


# 11: Create five stars using string repetition.

a = "*" * 5
print(a)

# Output:
# *****


# 12: Print a word with three stars on both sides.

s = "Python"
print("*" * 3 + s + "*" * 3)

# Output:
# ***Python***


# 13: Find and print the length of a string.

a = "Ravi"
print(len(a))

# Output:
# 4


# 14: Print the first character of a string.

a = "Ravi"
print(a[0])

# Output:
# R


# =====================================
# 5. User Input and Output
# =====================================

# 15: Take a username and age as input, then print a sentence using both.

username = input("Enter your name: ")
age = input("Enter your age: ")

print(username + " is " + age + " years old.")

# Sample Input:
# Vishnu
# 20

# Output:
# Enter your name: Vishnu
# Enter your age: 20
# Vishnu is 20 years old.


# 16: Read two numbers and print their sum.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)

# Sample Input:
# 10
# 20

# Output:
# Enter first number: 10
# Enter second number: 20
# 30


# 17: Read two numbers and print sum, difference, product, and quotient.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)

# Sample Input:
# 10
# 20

# Output:
# Enter first number: 10
# Enter second number: 20
# Sum: 30
# Difference: -10
# Product: 200
# Quotient: 0.5


# 18: Read a number and print its square and cube.

num = int(input("Enter a number: "))

print("Square:", num ** 2)
print("Cube:", num ** 3)

# Sample Input:
# 5

# Output:
# Enter a number: 5
# Square: 25
# Cube: 125


# 19: Read length and breadth, then print area and perimeter of a rectangle.

length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area:", area)
print("Perimeter:", perimeter)

# Sample Input:
# 10
# 5

# Output:
# Enter length: 10
# Enter breadth: 5
# Area: 50
# Perimeter: 30


# 20: Read radius and print the area of a circle.

radius = float(input("Enter radius: "))

area = 3.14 * radius * radius

print("Area:", area)

# Sample Input:
# 5

# Output:
# Enter radius: 5
# Area: 78.5


# 21: Read marks in 3 subjects and print total and average.

mark1 = int(input("Enter mark 1: "))
mark2 = int(input("Enter mark 2: "))
mark3 = int(input("Enter mark 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("Total:", total)
print("Average:", average)

# Sample Input:
# 80
# 90
# 70

# Output:
# Enter mark 1: 80
# Enter mark 2: 90
# Enter mark 3: 70
# Total: 240
# Average: 80.0


# 22: Read a temperature in Celsius and convert it to Fahrenheit.

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Fahrenheit:", fahrenheit)

# Sample Input:
# 25

# Output:
# Enter temperature in Celsius: 25
# Fahrenheit: 77.0

