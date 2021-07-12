
#Default Animal Class to extend with inheitance 

#This class acts as a interface - blueprint to make versiosn of 
class Animal:
    Fur_Colour = "Orange"

    def speak(self):
        print("RAAWWWRRR")
        #Could do raise NotImplementedError

    def eat(self):
        pass
    
    def chase(self):
        pass

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



tiger = Tiger()
tiger.speak()

cat = Housecat()
cat.speak()

print(cat.Fur_Colour)
