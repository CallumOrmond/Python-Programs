
#Default Animal Class to extend with inheitance 

#Using subclass to show how to overdide and access parent methods and varibles 

#This class acts as a interface - blueprint to make versiosn of 
class Animal:
    Fur_Colour = "Orange"

    def speak(self):
        print("RAAWWWRRR")
        #Could do raise NotImplementedError

    def eat(self):
        print("I am eating")
    
    def chase(self, animal="Gazelle"):
        print("I am chasing", animal)

#Extends animal class - has chase, speak, eat etc.
class Tiger(Animal):

    #Override SuperClass Animal
    def speak(self):
        print("They're Great!")

class Housecat(Animal):

    Fur_Colour = "black"

    #Override SuperClass Animal
    def speak(self): 
        print("Meow")

    def eat(self):
        super().eat() #right way
        print("I am eating salmon")

    def chase(self, animal):
        super().chase(animal)
        print(animal, "was caught")


tiger = Tiger()
tiger.speak()

cat = Housecat()
cat.speak()

cat.eat()

cat.chase("mouse")

print(cat.Fur_Colour)
