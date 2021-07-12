from tkinter import *
import time
import random

root = Tk()

default_color = "black"
active_color = "red"

StratLocation = (3,3)

D = []
CurrentPos = StratLocation
SnakeLocation = [CurrentPos]
SnackLocation = None

xSize = 20
ySize = 20

LvlUp = False
Game = False
Pause = False

#GAME STATE - Fix the death from 180ing too fast, death from self collision since left the down by passes the anti 180
#ADDITIONS  - Replay, Size/Speed Change in game
#HOW IT WORKS - S = Start, P = Pause, Q = Quit - all working


#########################
#GUI/Button Setup       #
#########################

for x in range(xSize):
	column = []
	for y in range(ySize):
		btn = Button(root, bg=default_color, padx=7, pady=0)
		btn.grid(row=y, column=x)
		column.append(btn)
	D.append(column)

D[StratLocation[0]][StratLocation[1]]["bg"] = active_color


#############################
# Actions + validation      #
#############################


def Down(D,pos):
	global CurrentPos

	if pos[1] >= ySize - 1:
		GameOver()
	else:
		#D[pos[0]][pos[1]]["bg"] = default_color
		D[pos[0]][pos[1]  + 1]["bg"] = active_color
		CurrentPos = (pos[0], pos[1] + 1)
			

def Up(D,pos):
	global CurrentPos

	if pos[1] <= 0:
		GameOver()
	else:
		#D[pos[0]][pos[1]]["bg"] = default_color
		D[pos[0]][pos[1]  - 1]["bg"] = active_color
		CurrentPos = (pos[0], pos[1] - 1)
	
		
def Right(D,pos):
	global CurrentPos

	if pos[0] >= xSize - 1:
		GameOver()
	else:
		#D[pos[0]][pos[1]]["bg"] = default_color
		D[pos[0] + 1][pos[1]]["bg"] = active_color
		CurrentPos = (pos[0] + 1, pos[1])
	
		

def Left(D,pos):
	global CurrentPos

	if pos[0] <= 0:
		GameOver()
	else:
		#D[pos[0]][pos[1]]["bg"] = default_color
		D[pos[0] - 1][pos[1]]["bg"] = active_color
		CurrentPos = (pos[0] - 1, pos[1])




###########################################
# Change Direction from Key Input         #
###########################################

CurrentDirection = Right

def Direction(Direction):
	global CurrentDirection
	
	Direction = Direction.char
	Actions = {"a" : Left, "s" : Down, "d" : Right, "w" : Up}
	L = {Left : "d", Down : "w", Right : "a", Up : "s"}

	if L[CurrentDirection] != Direction:
		CurrentDirection = Actions[Direction]

#########################
#GameOver               #
#########################

def GameOver():
	global Game
	Game = False

	print("GameOver")

	for i in range(5):
		for square in SnakeLocation:
			D[square[0]][square[1]]["bg"] = default_color

		root.update()
		time.sleep(0.75)

		for square in SnakeLocation:
			D[square[0]][square[1]]["bg"] = active_color

		root.update()
		time.sleep(0.75)

	Quit()

def GenerateSnack():
	global SnackLocation

	while True:
		Snackx = random.randint(0,19)
		Snacky = random.randint(0,19)

		if (Snackx, Snacky) not in SnakeLocation:
			SnackLocation = (Snackx, Snacky)
			D[Snackx][Snacky]["bg"] = active_color
			break

def Pause():
	global Game
	global Pause

	if Pause == True: #UnPause
		print("Unpause")
		Pause = False
		Game = True
		Play()
	else:             #Pause
		print("Paused")
		Pause = True
		Game = False

def Win():
	WinWindow = Toplevel(root)
	WinWindow.title("Winner!")
	WinWindow.geometry("150x50")
	Label(WinWindow, text="Congratz! You Win!").pack()
	Button(WinWindow, text="Quit", command=Quit).pack()


def Quit():
	Pause()
	root.destroy()






####################################################################################
# Main Loop         															   #
####################################################################################

def Start():
	global Game

	Game = True
	GenerateSnack()
	Play()

def Play():
	global Game
	global LvlUp
	global LastPosRed
	
	while Game == True:
		#Extend - Don't update last position if LvlUp is False - 
		#Else it won't update LastPosRed so will be 1 behind then set LvlUp to False so it wil update next loop
		
		CurrentDirection(D, CurrentPos) #Funtion call to move square - Updates CurrentPos

		if CurrentPos in SnakeLocation: #Checks if Snake hits self
			GameOver()

		SnakeLocation.append(CurrentPos) #List of Snake
		D[SnakeLocation[0][0]][SnakeLocation[0][1]]["bg"] = default_color #set last squre in list to black - creates tail of snake 


		#Cause Extension 
		if CurrentPos == SnackLocation:
			if len(SnackLocation) == 400:
				Win()
			GenerateSnack()
			LvlUp = True

		#if update is true then sont delete last element in list so the snake get longer
		#if it doesn't delete the last element then lvl is set to  false so that it del the last element next loop
		if LvlUp != True:
			del SnakeLocation[0]
		else:
			LvlUp = False

		#loops checking for input
		for i in range(10):
			time.sleep(0.01)
			root.update() #update location visually 

#########################
#Extra Buttons          #
#########################


btnUpDate = Button(root, text="S", command=Start)
btnUpDate.grid(row=21, column=0)

btnPause = Button(root, text="P", command=Pause)
btnPause.grid(row=21, column=1)

btnQuit = Button(root, text="Q", command=Quit)
btnQuit.grid(row=21, column=2)


root.bind('<KeyPress>', Direction)
mainloop()



