# def calc_sum(a,b):
#     sum=a+b
#     print(sum)
# calc_sum(5,9)
# calc_sum(5,-9)


# Average of three numbers
# def cal_avg(a,b,c):
    # sum1=a+b+c
    # avg=sum1/3
    # print(avg)
    # return avg
# cal_avg(4,5,6)
# print(cal_avg(5,8,9))

# def cal_prod(a, b=2):
#     print(a*b)
#     return a*b
# cal_prod(3)

# Write a function to print the length of a list(list is the parameter)
cities=["delhi","gurgaon","noida","pune","mumbai","chennai"]
def print_len(list):
    print(len(list))
print_len(cities)
print_len(cities)
# Write a function to print the element of a list in a single line.(list is the parameter)
def print_line(list):
    for item in list:
        print(item,end=" ")
print_line(cities)
print("\n")

# Write a function to find the factorial of n.(n is the parameter)
def fact(n):
    facto=1
    for i in range(1,n+1):
        facto*=i
    return facto
print(fact(5))
print(fact(6))


# Write a function to convet USD to INR
def USD(nudollar):
    return nudollar*83
print(USD(5))
print(USD(6))