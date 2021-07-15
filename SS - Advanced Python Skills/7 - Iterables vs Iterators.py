#iterable is a series of elements that can be iterated over - but does not have a state 
#They can be converted with iter(list, etc.)
#Iterator is a object with iteration state --> uses next() and __next__() --> like objects produced from filter, zip, etc.

fruits = ["apples", "pineapple", "grapes", "lemon", "watermelon"]

fruits = iter(fruits)

print(next(fruits))

print(fruits.__next__(), "\n")

#NOTES
#   -Nothing



#EXTRA --> HOW FOR LOOPS WORK

fruits = ["apples", "pineapple", "grapes", "lemon", "watermelon"]
fruits = iter(fruits)

while True:
    try:
        elm = next(fruits)
        print("FOR LOOP - ", elm)
    except StopIteration:
        break
