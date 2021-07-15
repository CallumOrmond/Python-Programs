#Applies a funtion to each item in iteratble 
#Returns map object
#Advanced for loop - use instead of loops 

#Aim capitize each work in list

#FOR LOOP
fruits = ["apples", "pineapple", "grapes", "lemon", "watermelon"]
result = []
for fruit in fruits:
    result.append(fruit.capitalize())
print(result)

#MAP
fruits = ["apples", "pineapple", "grapes", "lemon", "watermelon"]
result = map(lambda fruit: fruit.capitalize(), fruits)
print(list(result))

#OR 

def cap(fruit):
    return fruit.capitalize()

fruits = ["apples", "pineapple", "grapes", "lemon", "watermelon"]
result = map(cap, fruits)
print(list(result))


#NOTES
#   -Syntax map(Funtion, List)
#   -Can have any funtion