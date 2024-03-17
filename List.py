# List -> A built in data type that stores set of values
# It can store elements of different types (integer, float, string, etc.)
# Lists are mutable
# marks=[94.4, 87.5, 95.2, 66.4, 45.1]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[1:])
# print(marks[-2:])
# print(len(marks))
# students=["karan",85,"delhi",18]
# print(students[5]) # -=>It will give error

list1=[2,5,8,4,9,942,5,89,5]
list1.append(85)# Add one element at the end
list1.sort()# SOrts in ascending order
list1.sort(reverse=True)# sorts in descending order
list1.reverse() # reverse list
# list1.insert(idx,el) # insert element at index
list1.insert(3,55)

list2=[2,1,3]
list2.insert(1,5)
print(list2)

list3=[2,1,3,1]
list3.remove(1)# removes first occurrence of the element
list3.pop(2) #removes element at index