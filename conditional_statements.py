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
