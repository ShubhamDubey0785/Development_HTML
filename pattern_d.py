# 1
# 1 2
# 1 2 3 
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
x=8
for i in range(1,x):
    for j in range(1,i):
        print(j,end=" ")
        j+=1
    print(" ")