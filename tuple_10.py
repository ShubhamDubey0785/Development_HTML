c=(45,45,45,4,45,45)
i=0
c=""
while i<len(c):
    if c[i]!=c[i-1]:
        c="True"
        break
    else:
        c="True"
    i+=1
print(c)