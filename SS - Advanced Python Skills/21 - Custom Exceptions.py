#We can deine our own execption in python by inheriting the exception class

import random

number = random.randint(1,10)

class NumTooSmall(Exception):
    pass

class NumTooBig(Exception):
    pass

while True:
    try:
        n = int(input("Enter Number Here: "))
        if n < number:
            raise NumTooSmall("The Number Enetered is too small")  
        if n > number:
            raise NumTooBig("The Number Enetered is too big")
        else:
            print("you Guessed Right!")
            break

    except NumTooSmall as error:
        print(error)
    except NumTooBig as error:
        print(error)
    except ValueError:
        print("Enter a Number")

#NOTES 
#   -This Example is syntax 