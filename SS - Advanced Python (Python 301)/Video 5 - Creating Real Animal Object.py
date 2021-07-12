
#Default Animal Class to extend with inheitance 
class Animal:
    Fur_Colour = "Orange"

    def speak(self):
        print("RAAWWWRRR")

    def eat(self):
        pass
    
    def chase(self):
        pass

tiger = Animal()
tiger.eat()
tiger.chase()
tiger.speak()

