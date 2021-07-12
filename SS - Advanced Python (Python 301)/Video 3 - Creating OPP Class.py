#create class
class Animal:
    property_1 = {
        "key1" : "value 1"
    }
    _this_is_private = "Private String Cause of underscore"

TheAnimal = Animal()

#can access the property either way
print(TheAnimal.property_1["key1"])
print(Animal.property_1["key1"])