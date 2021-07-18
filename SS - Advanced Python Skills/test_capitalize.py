from typing import Type
#Test Driven Programming Steps:
#   1 - Write failing test
#   2 - Make the test pass
#   3 - Refactor the code - make it better making sure it still passes the tes 

#Rubbish for small project takes more time 
#Great for big projects - When you cant think about evey bit of code etc.

#TO USE PYTEST

#Create file called test_"something"
#import pytest
#create functions called test_"something"
#use assestions in the functions to perform the test
#call pytest in terminalto run tests


import pytest

def capital_case(string):
    if type(string) != str:
        raise TypeError("Argument must be String")
    return string.capitalize()

def test_capital_case():
    assert capital_case("david") == "David"

#If passing a number we expect a TypeError - So does not fail 
def test_is_string():
    #check that is the error we get
    with pytest.raises(TypeError):
        capital_case(1)