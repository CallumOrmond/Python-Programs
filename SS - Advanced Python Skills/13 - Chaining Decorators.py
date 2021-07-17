#Decorators can be combined and stacked
#Order matters 
#Exmaple from Django --> @login_required --> its a decorator to validate the users is loged in before calling the function

#EXMAPLE 1 - Flask Intro

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

#EXAMPLE 2

def wrapper1(f):
    def inner(*args, **kwargs):
        print("I am the first decorator")
        f(*args, **kwargs)
        print("I am the end of the first decorator")
    return inner

def wrapper2(f):
    def inner(*args, **kwargs):
        print("I am the second decorator")
        f(*args, **kwargs)
        print("I am the end of the second decorator")
    return inner

@wrapper2
@wrapper1
def hello_world():
    print("Hello World!")

hello_world()
print("\n")

@wrapper1
@wrapper2
def hello_world():
    print("Hello World!")

hello_world()

#NOTES 
#   -Order Matters 
#   -Unlimited Stack count - maybe?