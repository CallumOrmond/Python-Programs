#ANY --> Returns True if any value is True Otherwise False

#ALL --> Retuens True if all values are True Otherwise False

lst_True = [False, True]
print(any(lst_True), all(lst_True), " - True list")

lst_False = [False, False]
print(any(lst_False), all(lst_False), " - False list")

#Can use with map + lambda to for better use 
fruits = ["apples", "pineapple", "grapes", "lemon", "watermelon"]
fruits_mapped = map(lambda fruit : fruit.startswith("a"), fruits)
fruits = list(fruits_mapped)

print(any(fruits), all(fruits), " - Better Example")

#NOTES
#   -Nothing