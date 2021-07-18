#A counter if a type of dict (subclass)
#Collection where the elements are the keys adn their count is the value 

from collections import Counter

fruits = ["apple", "apple", "apple", "pineapple", "grape", "grape",]
count = Counter(fruits)

print(count)
print(count.get("apple"))
print(count.get("apple"))
print(count["apple"])
print(count["apples"])

print(count.most_common(1))

countString = Counter("Callum")
print(countString)

#NOTES
#   -Can be any value for count even negitive 
#   -More Methods in Doc