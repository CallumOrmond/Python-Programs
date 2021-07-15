#Function that wraps around another funtion - Similar to the design pattern - Coffee 2nd year

#Not sure why you would use this 
#Use - When you like My_Funtion but want to add more Functionality
def Decorator(func):
    def wrapper():
        print("Do Something")
        func()
        print("Original function is finished")
    return wrapper

@Decorator #Want to keep this function but add something to it 
def My_Function():
    print("hello world")


My_Function()
