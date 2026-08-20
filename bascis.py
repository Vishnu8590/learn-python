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

#string slicing



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

#23 Kilometers to Meters

a= float(input())
print("meters: ",a*1000)

#input:
#1.2


#output:
#1200



# =====================================
# 6. Relational Operators
# =====================================

#comparing Numbers
#----------------------

print(5>6)

#output:
#False
print(1.2<3.2)

#output:
#True

print(2 <= 2)
#output:
#True

print(2.2 != 3.2)
#Output:
#True

#Comparing String
#--------------------

print("ABC"=="ABC")
#output
#True

print("abc" == "ABC") #case sensitive
#ouput
#False


#? Check if first three characters of he two strings are same
str1 = input()
str2 = input()

print(str1[:3] == str2[:3])

#Input
#Application
#Apple

#Output
#True


#? Checks if the fist letter and last letter of the word are not same

word = input()
word_len = len(word)
first_letter = word[0]
last_letter = word[word_len - 1]
print(first_letter != last_letter)


#Sample Input:
#Python

#Output:
#True

#Sample Input:
#label

#Output:
#False

#? True should be printed if the sum of the digits of the two digit number N is gerater than 7,otherwise False should be printed

N = input()
firstNo = int(N[0])
secondNo=int(N[1])
print((firstNo+secondNo)>7)

#Sample Input:
#45

#Output:
#True


#? True should be printed if the second word is the last part of the first word,otherwise False should be printed

first = input()
second = input()

first_len = len(first)
second_len = len(second)

start_index = first_len -second_len

print(first[start_index:]==second)

#Sample Input:
#Blackhole
#hole

#Ouput:
#True

#? True should be printed if the word B starts at index I of the word A,otherwise False should be printed

A = input()
B = input()
B_len = len(B)
index = int(input())
end_index=index+B_len

print(A[index:end_index]==B)

#Sample Input:
#Repeat
#pea
#2

#Output:
#True

#? True should be printed if the N characters of the string and the last N characters of the string are not the same,otherwise  false should be printed.

string = input()
N = int(input())
length = len(string)
first_part = string[:N]
second_part = string[length-N:]

print(first_part != second_part)

#Sample Input:
#bulb
#1


#Output:
#False


# =====================================
# 7. Logical Operators
# =====================================

# and
# or
# not

print((4<5)and(not(1 != 1)))

#Output:
#True


#? True should be printed if the sum of A and B is not gerater than 100,otherwise False should be printed

a=int(input())
b=int(input())
sum= a + b 
greater=sum > 100
print(not(greater))


#Sample input:
#30
#20

# Output:
#True

#Sample Input:
#60
#70

#Output:
#False



#? True should be printed if both the given numbers are negative,otherwise False should be printed
a=int(input())
b=int(input())
print(a < 0 and b < 0)

#Sample Input:
# -1
# -2

#Output:
#True

#?  True should be printed if both A and B are positive numbers or both A and B are less tahn 70,otherwise False should be printed

a=int(input())
b=int(input())
positive=(a > 0)and(b > 0)
less_than=(a < 70)and(b <70)
print(positive or less_than)

# Sample Input:
# 200
# 50

# Output:
# True

