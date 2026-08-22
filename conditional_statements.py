#-------------------------------------------------
# If Statements
#-------------------------------------------------

a = int(input())
b = int(input())

if a > b:
    print(a-b)
print(a+b)


#Sample Input
# 1
# 2


#Output
#3

#? Write a program to convert the given integer into positive integer and print it

a = int(input())
if a < 0 :
    a = a*(-1)
print(a)


#Sample Input
#-2

#Output
#2


#-----------------------------------------------------
# If -else Statements
#----------------------------------------------------
a = int(input())
if a>0:
    print("Positive")
else:
    print("Negative")
print("End")

#Input:
#-1

#Output:
#Negative
#End


#? Zero should be printed if the given number is equal to 0.Positive should be printed if the given number is greater tahn 0.Negative should be printed if the given number is less than 0.

a = int(input())
if(a == 0):
    print("Zero")
elif(a>0):
    print("Positive")
else:
    print("Negative")


#Sample Input:
# 0
# 1
# -1


#Output:
# Zero 
# Positive
# Negative


#? Greatest among three numbers

a = int(input())
b = int(input())
c = int(input())

if a>b:
    greatest_Number = a
else:
    greatest_Number = b
if c>greatest_Number:
    greatest_Number = c
print(greatest_Number)


#Sample Input:
# 2
# 5
# 7

#Output:
# 7

#? Write a program reads two numbers and checks if one of the below condition is satisfied
# . One of A and B is equal to 6.
# . The sum of A and B is equal to 6.
# . The difference between A and B is equal to 6.

# print Lucky if the one of the given conditions is satisfied.Otherwise,print Not Lucky

a = int(input())
b = int(input())

equal_to_6 = a == 6 or b == 6 
sumof = a + b == 6
diff= a-b  == 6 or b-a == 6

if(equal_to_6 or sumof or diff):
    print("Lucky")
else:
    print("Not Lucky")


# Sample Input:
# 4
# 10

#Output:
# Lucky

#? A company decided to give a bonus of 5% to an employee if his/her years of service is more than five years.
# Write a program that reads an employee's salary and years of service and decides whether the employee gets the bonus or not.

s = int(input())
y = int(input())

bonus_amount = s*0.05
if y >5:
    print(bonus_amount)
else:
    print("No Bonus")

#Sample Input:
#25000
# 3

#50000
#6

#Output:
#No Bonus

#2500.0