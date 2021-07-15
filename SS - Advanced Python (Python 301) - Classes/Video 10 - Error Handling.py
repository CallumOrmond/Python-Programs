
#Basic layout
try:
    print("trying 1/0")
    total = 1/0
    print("This will not show up")
except Exception:
    print("Exception was caught")
    total = 0

#Real life Example 
num = input("What is a number")
try:    
    num = int(num)
except Exception: #Exception = type of exception to catch - in this case its any exception 
    num = "Unknow"

print(num) 