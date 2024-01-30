x=int(input())
l=[]
for i in range(x):
    c=input()
    l.append(c)
s=[]
for i in range(x):
    c=input()
    s.append(c)
print(dict(zip(l,s)))