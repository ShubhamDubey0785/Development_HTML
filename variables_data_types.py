# A variable is a name given to a memory location
# name="Rahul"
# age=18
# price=25.25
# print(name)
# print(age)
# print(price)
# age1=age
# print(age1)
# print("My name is: ", name)
# print("My age is: ",age)

# Rules for identifier
#       a-z, A-Z, underscore(_), and special sybbol are not allowed
# MeaningFull
# Can be of any length

# print(type(name))
# print(type(age))
# print(type(price))

# Data Types
# Integer +ve, -ve, 0
# String  (''), (""),('''...''')
# Float  3.99, 2.5, 9.0
# Boolean  True, False
# None

# name1="Rhul"
# name2='Rhul'
# name3='''Rhul'''
# print(name1)
# print(name2)
# print(name3)

# age5=23
# old=False
# tg=None
# print(type(age5))
# print(type(old))
# print(type(tg))

# Case Sensitive

# a=55
# b=11
# sum=a+b
# diff=a-b
# print(sum)
# print(diff)

# Types of Tokens
# Punctuators
# Punctuators are symbols to organize sentence structure in programming
# (), {}, [], # etc.
# Python is a Implicit typed language

# Expression Execution

# String & Numeric values can operate together
# A,B=2,3
# Txt="@"
# print(2*Txt*3)

# String and string can operate with +(Concatenation)
# A,B="2",3
# Txt="@"
# print((A+Txt)*B)

# Numeric values can operate with all arithmetic operator
# A,B=2,3
# C=4
# print(A+B*C)

# Arithmetic expression with Integer and Float will result in float
# A,B=10,5.0
# C=A*B
# print(C)

# Result of division operator with two integer will be float
# A,B=1,2
# C=A/B
# print(C)

# Integer division with float and int will give int displayed as float
# A,B=1.5,3
# C=A//B
# print(C,A/B)

# Floor gives closest integer, which is lesser than or equal to the float value
# Result of (A//B) is same as floor(A/B)

# A,B=12,5
# C=A//B
# print(C)

# A,B=-12,5
# C=A//B
# print(C)

# A,B=12,-5
# C=A//B
# print(C)

# Remainder is negative when denominator is negative
# A,B=-5,2
# C=A%B
# print(C)

# A,B=5,2
# C=A%B
# print(C)

# A,B=5,-2
# C=A%B
# print(C)

# Comment in Python
# single line comment
# """This is
#    a multi-line
#    comment"""

# Input in Python
# input() statement is used to accept values(using keyboard) from the user

# string input
# name=input("name: ")
# print(name)

# int input
# number=int(input("number: "))
# print(number)

# float input
# float1=float(input("name: "))
# print(float1)


name=input("Name: ")
age=int(input("Age: "))
price=float(input("Price: "))
print("My name is ",name," and I am ", age," years old")