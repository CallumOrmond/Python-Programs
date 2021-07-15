#Filters iterable based on conditions from a funtion

fruits = ["apples", "pineapple", "grapes", "lemon", "watermelon"]

#With lmabda 
filtered_fruits = filter(lambda fruit: fruit.startswith("a") , fruits)
print(list(filtered_fruits))

#with funtions 
def startswith_A(fruit):
    return fruit.startswith("a") 

filtered_fruits = filter(startswith_A, fruits)
print(list(filtered_fruits))

#Dict Exmaple
fruits = {"apple" : 10, "watermelon" : 50, "pineapple" : 45, "grapes" : 20}
filtered_fruits = dict(filter(lambda fruit : fruit[1] > 20, fruits.items()))
print(filtered_fruits)

#NOTES 
#   -Can cast the filtered object to dict when filtering a dict 
#   -