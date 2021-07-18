#Mathimatical Operations can be done on the sets
  
fruits = ["apple", "apple", "apple", "pineapple", "grape", "grape",]
fruits_set = set(fruits)

another_fruit_set = {"apple", "lemon", "lime", "pineapple"}

#Operations

a = another_fruit_set.issubset(fruits_set)
print(a)

a = another_fruit_set.issuperset(fruits_set)
print(a)

#UNION
a = another_fruit_set | fruits_set  #OR
a = another_fruit_set.union(fruits_set)
print(a)

#INTERSECTION
a = another_fruit_set & fruits_set #OR
a= another_fruit_set.intersection(fruits_set)
print(a)

#DIFFERENCE
a = another_fruit_set - fruits_set #OR
a = another_fruit_set.difference(fruits_set)
print(a)

#SYMETRIC DIFFERENCE
a = another_fruit_set ^ fruits_set
a = another_fruit_set.symmetric_difference(fruits_set)
print(a)




#NOTES 
#   -Union nad Intersection leave the sets unchanged unless use |= 
#   -_update after word to update the set on the left --> the one the call is acting upon

