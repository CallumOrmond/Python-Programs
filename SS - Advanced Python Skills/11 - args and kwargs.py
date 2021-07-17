#Pass a variable as 
# *args - argument --> pass a random number of arguments which are encapsulated in a tuple

def add(*args): #*args type = tuple 
    return sum(args)

a = add(1,2)
b = add(1,2,3,4,5,67)
c = add()
print(a, b, c)

# *kwargs - key-word argument -->pass a random number of arguments which are encapsulated in a dict with the passed name 

def print_fruits(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
    

d = print_fruits(apple=60, pear=50, watermelon=100)
e = print_fruits()
f = print_fruits(cherry=10)

#NOTES
#   -Very Simple