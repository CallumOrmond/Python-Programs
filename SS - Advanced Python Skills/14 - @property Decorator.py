#Helps us define Setters and Getters for classes in a nice way
#Makes attrubites private in class 
#Best ways at bottum

#EXMAPLE 1 - Normal Class

class Person:
    def __init__(self, age):
        self.age = age
    def category(self):
        if self.age < 13:
            return "kid"
        elif self.age >= 13 and self.age < 18:
            return "Teen"
        elif self.age >= 18:
            return "Adult"
        else:
            return "Bugged"

person = Person(22)
a = person.category()
print(a)

person.age = 55
a = person.category()
print(a)

person.age = -4
a = person.category()
print(a)

#doesnt make sense without validation --> someone else my be using this code and not know 

#EXMAPLE PART 2 - Modified Class
print(" \n EXAMPLE PART 2")

class Person:
    def __init__(self, age):
        self.set_age(age)

    def get_age(self):
        print("getting age")
        return self._age #_age is a convention --> means age is private, only touched with Getters and Setters

    def set_age(self, age):
        if age < 0:
            print("Age cannot be negitive")
        else:
            print("Setting age...")
            self._age = age

    def category(self):
        if self._age < 13:
            return "kid"
        elif self._age >= 13 and self._age < 18:
            return "Teen"
        elif self._age >= 18:
            return "Adult"
        else:
            return "Bugged"

person2 = Person(22)
print(person2.get_age())

person2.set_age(12)
print(person2.get_age())

print(person2.category())

#Can still change age with person2._age = 55
#EXMAPLE PART 3 
print("\n EXAMPLE PART 3")

class Person:
    def __init__(self, age):
        self.age = (age)

    def get_age(self):
        print("getting age")
        return self._age #_age is a convention --> means age is private, only touched with Getters and Setters

    def set_age(self, age):
        if age < 0:
            print("Age cannot be negitive")
        else:
            print("Setting age...")
            self._age = age

    def category(self):
        if self.age < 13:
            return "kid"
        elif self.age >= 13 and self.age < 18:
            return "Teen"
        elif self.age >= 18:
            return "Adult"
        else:
            return "Bugged"

    age = property(get_age, set_age)

person3 = Person(22)

#Both work with property
person3.age = 13
person3.set_age(44)

#when self.age is called in the category function it calls get_age() hence the printing
person3.category()


#EXMAPLE PART 4 
print("\n EXAMPLE PART 4")

class Person:
    def __init__(self, age):
        self.age = (age)

    @property
    def age(self):
        print("getting age")
        return self._age #_age is a convention --> means age is private, only touched with Getters and Setters

    @age.setter
    def age(self, age):
        if age < 0:
            print("Age cannot be negitive")
        else:
            print("Setting age...")
            self._age = age

    def category(self):
        if self.age < 13:
            return "kid"
        elif self.age >= 13 and self.age < 18:
            return "Teen"
        elif self.age >= 18:
            return "Adult"
        else:
            return "Bugged"

   

person3 = Person(22)

#Both work with property
person3.age = 13
person3.age

#NOTES 
#   -Property is the way to make private attrubite in a class 
#   -last 2 Exmaple are best way to do it 
#   -_age is a convention --> means age is private, only touched with Getters and Setters