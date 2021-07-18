#Method that is bound to the class not the object
#work with class - its parameter is always the class itself 
#e.g - def class_method(class, args...)

#For Factory methods --> methods that retuern a class 

import datetime

class person:
    def __init__(self, age) -> None:
        self.age = age

    def display_age(self):
        print("age -",self.age)
    
    @classmethod
    def person_from_birth(cls, birthYear):
        claculated_age = datetime.date.today().year - birthYear
        return cls(claculated_age)


person1 = person(20)
person1.display_age()

person2 = person.person_from_birth(1998)
person2.display_age()

#Subclass of person that adds nothing 
class Employee(person):
    pass

employee = Employee.person_from_birth(1970)
employee.display_age()


#NOTES 
#   -doesnt require the creation of a class object 
#   -Create instance of class with a different setup 
#   -Similar to have another constuctor 
#   -Can create other classes and be inherited