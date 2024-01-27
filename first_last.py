# Write a python program to swap first and last element of the list
x=[1,2,3,4,5,6,7,8,9]
y=x[0]
x[0]=x[-1]
x[-1]=y
print(x)