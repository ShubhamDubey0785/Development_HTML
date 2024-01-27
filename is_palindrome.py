a=input("Enter a number here: ")
# x=[]
# count=0
# for i in range(a):
#     s=input(f"Enter your value {i+1} here: ")
#     x.append(s)
# for i in x:
#     if i.capitalize()==i[-1::-1].capitalize():
#         count+=1
# print(count)
c=a[-1::-1]
if c==a:
    print("Yes")
else:
    print("No")