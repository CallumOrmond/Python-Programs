
#Default Animal Class to extend with inheitance 

#Using subclass to show how to overdide and access parent methods and varibles 

#This class acts as a interface - blueprint to make versiosn of 
class Animal:
    Fur_Colour = "Orange"
    animal_type = "unknown"

    #constructor - Run First - takes params from objext creation
    def __init__(self, fur_colour):
        self.Fur_Colour = fur_colour
        
    def speak(self):
        print("RAAWWWRRR")
        #Could do raise NotImplementedError

    def eat(self):
        print("I am eating")
    
    def chase(self, animal="Gazelle"):
        print("I am chasing", animal)

    #getter 
    def get_fur_clour(self):
        print(self.Fur_Colour)


class Housecat(Animal):


    def __init__(self, fur_colour): #can override constructors - this just calls the original one 
        super().__init__(fur_colour)
        self.animal_type = "House Cat" # hard code - always housr cat 
        print("house cat constructor used")

    #Override SuperClass Animal
    def speak(self): 
        print("Meow")

    def eat(self):
        super().eat() #right way
        print("I am eating salmon")

    def chase(self, animal):
        super().chase(animal)
        print(animal, "was caught")

cat = Housecat("Orange")
cat.chase("mouse")
cat.get_fur_clour() #From above constuctor 

cat.get_fur_clour()

cat2 = Housecat("brown")

print("tewst")
