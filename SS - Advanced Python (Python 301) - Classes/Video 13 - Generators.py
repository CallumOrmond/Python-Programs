lst = [1,2,3]# always in memory 

#Generator is a way of doing something with the numbers regardless of the surrounding numbers and deleting the numbers after use
#Saves lot of memory - Number not good exmaple since they are small - made for big data sets 

def MyGen():
    for num in range(50):
        yield num ** num #yield makes the function a generator - uses the number then does not store in memory 
                         #if did not use yield then the numbers would be stored in mem and use loads
MyGenVar = MyGen()

all_numbers = list(MyGenVar)
print(all_numbers)

#does not print anything - since deleted after use when cast to list - one and done
for BigNum in MyGenVar:
    #prints one at a time instead of storing in mem
    print(BigNum)

