#Three things need for a closure
#1 - must have nested funtion
#2 - nusted funtion must refer to a value definied in enclosing funtion 
#3 - enclosing funtion msut return nested function

def print_message(msg):
    def printer():
        #msg is read only here --> use nonlocal keyword to access it 
        #nonlocal msg  
        print(msg)
    return printer

another_funtion = print_message("Hello")

another_funtion()

#When to use 
#Can avoid the use of global variables - provide some form of data hiding
#provide OO solution to problems --> Decorators

class multi:
    def __init__(self, n):
        self.n = n

    def multiply(self, x):
        return x * self.n

obj = multi(5)
a = obj.multiply(7)
print(a)

#Same thing in less code and dont need to make class

def mutliplier(n):
    def mul(x):
        return x * n
    return mul

mutliplier_by_5 = mutliplier(5)
b = mutliplier_by_5(7)
print(b)

#NOTES 
#   -Important for decorators