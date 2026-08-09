# 1. Display Message
print("Welcome to Python")

# Output:
# Welcome to Python


# 2. Basic Calculations
a = 10
b = 20
print("add:",a + b)
print("sub:",a-b)
print("mult:",a * b)
print("div:",a / b)


# Output:
# add: 30
# sub: -10
# mult: 200
# div: 0.5


# 1. Data Types
name = "Vishnu"
id=12.0
age = 20
is_learning_python = True


print(type(name))
print(type(id))
print(type(age))
print(type(is_learning_python))

# Output:
# <class 'str'>
# <class 'float'>
# <class 'int'>
# <class 'bool'>

#Defining a variable

a =10
print(a)

# Output:
#10

#variable Assignment
a=1
print(a)
a=2
print(a)

# Output:
# 1
# 2

#value in variable

a=1
b=2
a=b
print(a)
print(b)

# Output:
#2
#2

#Order of Operations(BODMAS)

print(10/2+3)

# Output:
#8.0

#Input and Output Basics

#Adding strings

a = "1"+"2"
print(a)

# Output:
#12

#String Concatenation

name = "Vishnu"
print("Hi "+name)

# Output:
#Hi Vishnu

a="*" + "*"
print(a)

# Output:
#**

a= "*" *5
print(a)

# Output:
#*****

#String Repetition

s ="Python"
print("*"*3 + s + "*"*3)

#Output
#***Python***


#Length of string
a="Ravi"
print(len(a))

# Output:
#4

#Take input from user

username= input()
age = input()
print(username +" is "+age+" years old.")

# Output:
#Vishnu is 20 years old

#Accessing Characters in string

a = "Ravi"
print(a[0])

#Output
#R