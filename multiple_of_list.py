x = list(map(int, input("Enter multiple values: ").split()))
print(x)
a=0
b=0
c=0
for i in x:
    if i%2==0:
        a+=1
    if i%3==0:
        b+=1
    if i%5==0:
        c+=1
# print(a)
# print(b)
# print(c)
r=[a,b,c]
s=[2,3,5]
print(dict(zip(s,r)))
# print("{'2':",a,",'3':",b,",'5':",c,"}")