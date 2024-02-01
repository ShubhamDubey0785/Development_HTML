# Write a python programto reverse the string and swap to small or capital in letter
a="The quick brown fox jumps over the lazy dog"
print(a.swapcase())
print(a[-1::-1])
print(a.split(" "))
w=a.split(" ")
print(w)
for i in range(len(w),0,-1):
    print(w[i-1],end=" ")