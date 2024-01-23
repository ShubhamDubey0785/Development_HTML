# write a python program to take a number from the user and check whether it is prime number or not
x=int(input())
c=0
for i in range(2,(x+1)//2):
    if x%i==0:
        c+=1
        break
    else:
        c=0
if c==1:
    print("it is not a prime number")
else:
    print("it is a prime number")