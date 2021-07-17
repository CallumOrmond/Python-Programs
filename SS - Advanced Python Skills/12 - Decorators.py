#In Python you can pass funtions to other funtions --> Higher Order Funtions
#Can return functions as well 
#   Decorators Take a function adds something to it and returns it 

#EXMAPLE 1
def wrapper(f):
    def inner():
        print("I am a decorated function")
        f()
    return inner

def hello():
    print("Hello World!")

decorated_Hello_World = wrapper(hello)
decorated_Hello_World()

#EXMAPLE 2
#OR BETTER WAY TO CALL --> instead of line 14 + 15

@wrapper
def hello2():
    print("Hello World Again!")

hello2()

#EXMAPLE 3
def wrapper2(f):
    def inner2(a, b):
        print("I am a decorated function Again")
        if b==0:
            print("cannot use 0")
            return
        else:
            return f(a, b)
    return inner2
        
@wrapper2
def divide(a, b):
    return a/b

@wrapper2
def complicated_operation(a, b):
    #lots of logic where b cannot == 0 -- for the sake of exmaple 
    return a/b 


divide(3, 0)
complicated_operation(5, 0)

#NOTES
#   -Have a main funtion that does something - and want to insert other function into it
#   -The inserted function can vary --> reason its not hard coded
#   -Reduces the amount of code --> can reuse
#   -Use *args/**kwargs to take in varible from funtion


#EXTRA EXAMPLE

import time

def wrapper(f):
    def inner(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        end = time.time()
        time_taken = end - start
        print("This funtion took", time_taken)
    return inner

@wrapper
def complex_operation(a,b,c):
    r = a+b+c
    r = r * a 
    r = r / c
    print(r)

complex_operation(5, 8, 19)