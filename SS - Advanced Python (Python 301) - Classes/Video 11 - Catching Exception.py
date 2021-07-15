num = input("Enter number ")
num2 = input("\n Enter a sencond number ")

try:
    num = int(num)
    num2 = int(num2)
    total = num/num2

#Python pickes the right error and runs that code
except ValueError:
    print(num, num2, "num or num2 were not valid numbers - ValueError")

except ZeroDivisionError:
    print("num2 was 0, number could not be divided - ZeroDivisionError")

except Exception as e: #gets the Exception and stores in e
    print("Exception was caught")
    print(type(e))
    num = "Unknown"

print(num)