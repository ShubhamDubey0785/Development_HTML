# Write a Python Program to Square Each Element of the List and Print List in Reverse Order
l=[1,2,3,4,5]
y=[]
for x in l:
    z=x*x
    y.append(z)
print(y[-1::-1])
