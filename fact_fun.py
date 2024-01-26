# wite a python program to find the factorial of a number using function

def fact_fun(n):
        if n==1:
                return 1
        else:
            return n*fact_fun(n-1)
print(fact_fun(5))