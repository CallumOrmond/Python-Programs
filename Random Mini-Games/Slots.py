import random
import time
import time 


#WORKING 
#Odds = 1/16

CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K'

Row1 = [ "J ", "Q ", "k ", "A ", ]
Row2 = [ "J ", "Q ", "k ", "A ", ]
Row3 = [ "J ", "Q ", "k ", "A ", ]
RowBlank = ["  ","  ","  ","  ",]


random.shuffle(Row1)
random.shuffle(Row2)
random.shuffle(Row3)

if (Row1[1] == Row2[1] and Row1[1] == Row3[1]):
	Winner = 1
else:
	Winner = 2

def Results(Row1, Row2, Row3, Winner=0):

	print("╔═════════╗")
	print("║ {0} {1} {2}║".format(Row1[0],Row2[0],Row3[0]))
	print("║ {0} {1} {2}║".format(Row1[1],Row2[1],Row3[1]))
	print("║ {0} {1} {2}║".format(Row1[2],Row2[2],Row3[2]))
	print("╠═════════╣")
	if Winner == 1:
		print("║ Winner! ║")
	elif Winner == 2:
		print("║  Loser  ║")
	else:
		print("║         ║")
	print("╚═════════╝")

def run(Row1, Row2, Row3, RowBlank):
	Results(RowBlank, RowBlank, RowBlank)
	time.sleep(0.3)
	Results(Row1, RowBlank, RowBlank)
	time.sleep(0.3)
	Results(Row1, Row2, RowBlank)
	time.sleep(0.3)
	Results(Row1, Row2, Row3)
	time.sleep(0.3)

	for i in range(10):
		time.sleep(0.5)
		Results(Row1, Row2, Row3, Winner)
		time.sleep(0.5)
		Results(Row1, Row2, Row3)


def ProbCheck():
	Row1 = [ "J ", "Q ", "k ", "A ", ]
	Row2 = [ "J ", "Q ", "k ", "A ", ]
	Row3 = [ "J ", "Q ", "k ", "A ", ]
	RowBlank = ["  ","  ","  ","  ",]


	random.shuffle(Row1)
	random.shuffle(Row2)
	random.shuffle(Row3)

	if (Row1[1] == Row2[1] and Row1[1] == Row3[1]):
		return 1
	else:
		return 0


run(Row1, Row2, Row3, RowBlank)