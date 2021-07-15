#Simple way to make iterators 
#yield - keyword

#get mext power of 2 
def powers_of_two(max=5):
    for i in range(max + 1):
        yield 2**i

powers = powers_of_two(5)

print(next(powers))
print(next(powers))
print(next(powers))
print(next(powers))
print(next(powers), "\n")

#Stops when yield id called -- Would be infinite loop otherwise -- infinte serise
def powers_of_2_While(max=5):
    i = 0
    while True:
        yield 2**i
        i += 1

powers = powers_of_2_While(5)

print(next(powers))
print(next(powers))
print(next(powers))
print(next(powers))
print(next(powers), "\n")

#Another Syntax 
numbers = [4,6,2]
powers = (x**2 for x in numbers)

print(next(powers))
print(next(powers))
print(next(powers))


#NOTES
#   -Local Varibles are remembered between calls
#   -Very memory efficient
#   -Stops when yield is called




