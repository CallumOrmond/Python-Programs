#create class
from abc import abstractproperty


class Animal:
    property_1 = {
        "key1" : "value 1",
    }

    this_list = ["gully", "kane", "John"]
    
    #add name to list 
    def add_name(self, name):
        self.this_list.append(name)
        return self.this_list

    #remove name from list
    def remove_name(self, name):
        if name in self.this_list:
            self.this_list.remove(name)
            print(name, "revmoved")
        else:
            print("does not contain", name)


    #just like normal method with self as param
    def This_is_a_method(self):
        #self allows access to the object - everything 
        print(self.this_list)
        
    #funtion treated as if its not a callable, thus does not need brackets to call, cant have input params 
    @property
    def get_gully(self):
        return self.this_list[0]


theAnimal = Animal()
theAnimal.This_is_a_method()

theAnimal.add_name("bill")
theAnimal.This_is_a_method()

theAnimal.remove_name("bill")
theAnimal.This_is_a_method()

gully = theAnimal.get_gully
print(gully, "says hello")

