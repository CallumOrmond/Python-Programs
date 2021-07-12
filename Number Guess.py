import random

#WORKING 

right = False

#Get the range and validate - cant be empty and has to be int 
randRange = input("Pick the range of your random guess : ")
while (not randRange.isdigit() or randRange == ""):
	randRange = input("Pick the range of your random guess : ")

#get randum number, get guess validate
while(right == False):
	randomNum = random.randrange(int(randRange)) + 1
	Guess = input("Pick a number between 1 and {randomNum} : ".format(randomNum=randRange))

	#Validate guess - has to be int, not empty and within the range
	while(not Guess.isdigit() or Guess == "" or Guess >= randRange):
		Guess = input("Pick a number between 1 and {randomNum} : ".format(randomNum=randRange) )
	
	#check gues
	if randomNum == int(Guess):
		print("your got it right!")
		right = True
	else:
		print("try again :(, the number was {correct} \n".format(correct=randomNum))