# 6 5 4 3 2 1
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1 
x=8
for i in range(x,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
        j-=1
    print(" ")