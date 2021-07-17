#sort --> mehtods only works for lists 
#sorted --> works for any iteratble

fruits = ["apples", "pineapple", "grapes", "lemon", "watermelon"]
#Changes List
print(fruits.sort(), fruits)



fruits = ["apples", "pineapple", "grapes", "lemon", "watermelon"]
#Does not chnage list --- Creates returns a new one 
print(sorted(fruits), fruits)  


def Second_Letter(fruit):
    return fruit[1]

fruits = ["apples", "pineapple", "grapes", "lemon", "watermelon"] #Don't Need
#Sorted based on return value of each list element in the funtion 
print(sorted(fruits, key=Second_Letter)) 
#OR
print(sorted(fruits, key= lambda fruit : fruit[1]))


#NOTES
#   -Can reverse both
#   -Can specify a key