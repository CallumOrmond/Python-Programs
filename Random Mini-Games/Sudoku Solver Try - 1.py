import pprint
import time

#SUMMARY
#WORKING BASED ON VIDEO FROM TECH WITH TIM 
#BACK TRACKING ALGORITM - GREAT EXAMPLE OF RECURSION 



board =[[5,3,0,0,7,0,0,0,0], 
	[6,0,0,1,9,5,0,0,0], 
	[0,9,8,0,0,0,0,6,0], 
	[8,0,0,0,6,0,0,0,3], 
	[4,0,0,8,0,3,0,0,1], 
	[7,0,0,0,2,0,0,0,6], 
	[0,6,0,0,0,0,2,8,0], 
	[0,0,0,4,1,9,0,0,5],
	[0,0,0,0,8,0,0,7,9]]


def printB(board=board):
	for i in board:
		print(i)
	print("-------------------")

def printBoardClean(board=board):
	for i in range(9):
		if i in [3,6]:
			print("\n---------------------")
		else:
			print()
		for j in range(9):
			if j in [3,6]:
				print("| ", end='')
				print(board[i][j], end='')
				print(" ",end='')
			else:
				print(board[i][j], end='')
				print(" ",end='')

	print()


def validFullBoard(board):
	#check rows
	Valid = True

	for row in board:
		if sorted(row) != [1,2,3,4,5,6,7,8,9]:
			Valid = False
			print("Row False", row)

	#check columns
	for i in range(9):
		l = []
		for row in board:
			l.append(row[i])
		if sorted(l) != [1,2,3,4,5,6,7,8,9]:
			Valid = False
			print("Column False", row)


	#check squares 
	#need to check row[1,2,3] + col[1,2,3]
	for right in range(3): #moves loop right to next 3x3
		for down in range(3): #moves loop down to next 3x3
			l = []
			for i in range(1,4): #loops first 3 rows
				for j in range(1,4): #loops 3 columns 
					l.append(board[i - 1 + (3 * down)][j - 1 + (3 * right)])

			if sorted(l) != [1,2,3,4,5,6,7,8,9]:
				Valid = False
				print("Box False", right, down)


	return Valid

def validPos(board, pos, value):
	#check rows <--->
	if value in board[pos[1]]:
		return False

	#check columns \//\
	for row in board:
		if value == row[pos[0]]:
			return False
			
	#check boxes 3x3
	#find 3x3 
	xbox = pos[0]//3
	ybox = pos[1]//3

	for i in range(xbox * 3, xbox *3 + 3):
		for j in range(ybox * 3, ybox * 3 + 3):
			if value == board[j][i]:
				return False

	return True




#finds next 0/empty squre from left to right then up to down 
def FindEmpty(board):
	for y in range(0,9):
		for x in range(0,9):
			if board[y][x] == 0:
				return (x,y)

	return False	

	
#main function to solve
def SolveSudoku(board, Show):
	
	pos = FindEmpty(board)
	if pos == False:
		return True	


	for i in range(1,10):
		if validPos(board, pos, i) == True:
			board[pos[1]][pos[0]] = i
			if SolveSudoku(board, Show):
				return True

			board[pos[1]][pos[0]] = 0

			if Show == True:
				printBoardClean()
				time.sleep(0.001)
	return False



SolveSudoku(board, False)

printB()

print(validFullBoard(board), "board correct!")
