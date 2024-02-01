# write a python program to find the smallest and largest number from a list
x=[]
y=int(input("How many number in the list: "))
for i in range(y):
    n=int(input())
    x.append(n)
print(x)
print(min(x))
print(max(x))