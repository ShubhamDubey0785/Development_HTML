# Dictionaries are used to store data in key:value pairs
# They are unordered, mutable(changeable) & don't allow duplicate keys

# dict={
#     "name":"Raj",
#     "age":18,
#     "city":"Agra",
#     "marks":(98,45,230),
#     "is_adult":True,
#     "subjects":["python","c++"],
# }
# print(dict)
# dict["name"]="RjaRatan Kumar"  # Over Write
# dict["surname"]="Singh"

# print("\n",dict)

# Empty dictionary
# null_dict={}
# null_dict["name"]="Hello duniya"
# print(null_dict)


# Nested dictionary
# student={
#     "name":"Rhul raj",
#     "score":{
#         "chem":98,
#         "phy":100,
#         "math":99
#     }
# }
# print(student)
# print(student["score"]["phy"])
myDict={
    "name":"Jiya",
    "subjects":{
        "phy":85,
        "che":87,
        "math":89,
    }
}
# print(myDict.keys()) #returns all keys
# print(len(myDict)) #returns length of dictionary
# print(list(myDict.keys())) #returns all keys in a list
# print(len(list(myDict.keys()))) #returns length of a list

# print(myDict.values()) #returns all values
# print(list(myDict.values())) #returns all values

# print(myDict.items()) #returns all(key, val) pairs as tuples
# pairs=list(myDict.items())
# print(pairs[0])

# print(myDict["name"])
# print(myDict.get("name"))
# print(myDict["name1"])  #-=>error
# print(myDict.get("name1"))  #-=> None
 
# myDict.get() # returns the key according to value
# new_dict={"name":"delhi","age":16}
# myDict.update(new_dict) #insert the specified items to the dictionaries
# print(myDict)
