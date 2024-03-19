# take input of age from 3 people
# determine the oldest and youngest
person1 = int(input("enter first age"))
person2 = int(input("enter second age"))
person3 = int(input("enter third age"))
if person1 > person2 and person1 > person3:
    print("oldest" ,person1)
elif person1 > person2 and person1 < person3:
    print("young" , person2)
elif person1 < person2 and person1 < person3:
    print("youngest" ,person3)