#Collection that is unordered and unindexed
#iterable and mutable (Can add more after creation)
#No dublicate elements

fruits = ["apple", "apple", "apple", "pineapple", "grape", "grape",]
fruits_set = set(fruits)
print(fruits_set)

another_fruit_set = {"apple", "lemon", "lime", "pineapple"}
print(another_fruit_set)

empty_set = set() #empty_set = {} --> creates Dict 
print(empty_set)

fruits_set.add("banana")
print(fruits_set)

fruits_set.update(["banana", "melon", "grape"])
print(fruits_set)

fruits_set.remove("banana")
print(fruits_set)
#To Aviod Error 
fruits_set.discard("banana")
print(fruits_set)

#Unordered --> Removes Random Element
fruits_set.pop()
print(fruits_set)

fruits_set.clear()
print(fruits_set)

#FROZEN SETS 
#Since sets are mutable they are unhashable --> cant use as dict key etc.
#Can make one unmutable freezing it 

frozen_set = frozenset([1,2,3,4,5,98,12])
print(frozen_set)

dict_empty = {frozen_set : "Key is a frozen set"}
print(dict_empty.items())
print(dict_empty[frozen_set])

#NOTES 
#   -Very Fast
#   -Based off Mathimatical representaion