import os
f=open("sample.txt","r")

# For open in binary mode
# f=open("sample.txt","rb")
# data=f.read()  # Read the entire content
# f.seek(0) # Move the pointer to the begining
# dat=f.read(5)
# print(data)
# print(dat)
# print(type(data))
# f.seek(0)
# line1=f.readline() # Reads one line at a time
# print(line1)
# f.close()

# f=open("sample.txt","a")
# # To overwrite the code
# f=open("sample.txt","r")
# f.write("\nI want to learn JavaScript tommorow. 12345")
# f.close()

# with open("sample.txt","r"):
#     data=f.read()
#     print(data)


os.remove("demo_delete.txt")