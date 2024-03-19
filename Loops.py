# count=1
# while count<=5:
#     print("hello")
#     count+=1

# cnt=1
# while cnt<=100:
#     print(cnt)
#     cnt+=1
# cnt=100
# while cnt>0:
#     print(cnt)
#     cnt-=1

# mul=1
# num=int(input("Enter number: "))
# while mul<11:
#     print(num*mul)
#     mul+=1

# nums=[1,4,9,16,25,36,49,64,91,100]
# idx=0
# while idx<len(nums):
#     print(nums[idx])
#     idx+=1

# nums1=(1,4,9,16,25,36,49,64,91,100)
# i=0
# x=36
# while i<len(nums1):
#     if(nums[i]==x):
#         print("Found at index: ",i)
#     else:
#         print("finding..")
#     i+=1 
# print("end of loop")

# i=0
# while i<=5:
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i+=1

# nums=[1,2,3,4,5]
# for val in nums:
#     print(val)

     
# Sstr1="The quick brown fox jumps over the lazy dog"
# for char in Sstr1:
#     print(char)

# stre="Hello Duniya"
# idx=0
# x='o'
# for el in stre:
#     if(el==x):
#         print("char found at idx: ",idx)
#         break
#     idx+=1

# print(range(5))
# seq=range(10)
# for i in seq:
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(2,10):
    # print(i)

# for i in range(2,10,2):
    # print(i)

# for i in range(5):
#     #empty
#     pass

# print("Some useful work..")

# Write a program to find the sum of first n numbers.(using while)
# num=int(input("Enter number: "))
# i=0
# sum=0
# while i<=num:
#     sum+=i
#     i+=1
# print(sum) 

# Write a program to find the factorial ofa number(using for)
fact1=int(input("Enter number: "))
fact=1
for i in range(1,fact1+1):
    fact*=i
print(fact)