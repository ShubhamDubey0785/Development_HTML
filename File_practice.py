# Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using java
# I like programming in Java.
with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java\nI like programming in Java")

f.close()

# Write a file that replace all occurrences of java with python in the above file

with open("practice.txt","r") as f:
    data=f.read()
new_data=data.replace("Java","Python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)


# Search if thr word "learning" exists in the file or not.
def check_for_word():
    word="learning"
    with open("practice.txt","r") as f:
        data=f.read()
        if(data.find(word)!=-1):
            print("Found..!")
        else:
            print("Not found..!")
check_for_word()

# Write a function in which line of the file does the word "learning" occur first.
# Print 1 if the word not found
def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return 
            line_no+=1
    return -1
check_for_line()

# From a file containing numbers separated by comma, print the count of even numbers.

