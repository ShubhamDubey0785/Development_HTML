x=int(input())
# c=1
# for i in range(1,x+1):
    # c=i*c
# print(c)
def fact(a):
    if a==1:
        return 1
    else:
        return a*fact(a-1)
print(fact(x))