#Adds counter to iteratable - returns enumerate object
#usefull for loops 

#makes tuple of the counter and the enumurated value (fruit)
fruits = ["apples", "pineapple", "grapes", "lemon", "watermelon"]

Counter_Start = 5
enumerated_fruits = enumerate(fruits, start = Counter_Start)
print(list(enumerated_fruits))


for index, value in enumerate(fruits):
    filename = f"file{index}.txt"
    #do something with file
    print(filename)

#NOTES
#   -Nothing So Far