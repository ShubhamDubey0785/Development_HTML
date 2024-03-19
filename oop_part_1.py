class Student:
    name="Raj ratan"
s1=Student()
print(s1)
print(s1.name)

class Car:
    color="Blue"
    brand="mercedes"
car1=Car()
print(car1.color)
print(car1.brand)

# __init__ function
class Student1:
    def __init__(self,fullname):
        print(self)
        self.name=fullname
        print("Adding new student in Database..")
s1=Student1("karnan")
print(s1.name)