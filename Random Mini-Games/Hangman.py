
#WOKRING USES INPUT 

def WordToList(word):
	return [char for char in word]

def play():

	#Word to Guess
	Word = input("Word to Guess : ").lower()
	while(not Word.isalpha() or len(Word) == 0):
		Word = input("Word to Guess : ").lower()

	WordList = WordToList(Word)					#Word as List
	CurrentLetters = ["_"] * len(WordList)		#Letters Guessed
	WrongCount = 0
	
	#Game Loop
	while("_" in CurrentLetters or WrongCount == 5):

		#Guess Letter
		Guess = input("Guess Letter : ").lower()	
		while(len(Guess) != 1 or not (Guess.isalpha())):
			Guess = input("Guess Letter : ").lower()

		#Check Guess
		if Guess in WordList:
			for i in range(len(WordList)):
				if WordList[i] == Guess:
					CurrentLetters[i] = Guess
					print("Current Letters :", CurrentLetters, 5 - WrongCount, "- Guesses Left", Guess, "- is correct \n")
			 
		else:
			WrongCount = WrongCount + 1
			print("Current Letters :", CurrentLetters, 5 - WrongCount, "- Guesses Left", Guess, "- is not in the word \n")


	if WrongCount == 5:
		print("The Word was", Word, "Try Again next time")
	else:
		print("Good job! The word was", Word) 

	return 
    
play()
