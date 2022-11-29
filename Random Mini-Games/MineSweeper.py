from itertools import count
from tkinter import * 
import random
import time
import numpy as np

root = Tk()
Size = 10
BombCount = 20

#############################
# Setup for Grid            #
#############################

#Create 2D Array to store Grid



def MakeEmptyGrid(Size, BombCount):

	#ISSUE : Not unique --- Fixed 06/07/2022 

	grid = np.zeros((Size, Size))
	


	for i in range(BombCount):
		randomx = np.random.randint(0, Size)
		randomy = np.random.randint(0, Size)

		while grid[randomx][randomy] == 1:

			randomx = np.random.randint(0, Size)
			randomy = np.random.randint(0, Size)

		grid[randomx][randomy] = 1
		
	return grid


grid = MakeEmptyGrid(Size, BombCount)


def GridBombCount(grid):
	print(grid)
	numGrid = np.zeros((Size, Size))
	offset = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
	
	#does everything aprat from edges and cornners 
	for j in range(Size):
		for i in range(Size):
			count = 0
			#coords = i, j
			for index in offset:
				if i + 1 <= Size and j + 1 <= Size and grid[i, j] != 1:
					if index[0] + i < Size and  index[1] + j < Size and index[0] + i >= 0 and  index[1] + j >= 0:
						if grid[index[0] + i, index[1] + j] == 1:
							print(j, i)
							count = count + 1
			
			numGrid[i, j] = count
		

	##check cornners 

	return numGrid
			


numGrid = GridBombCount(grid)
print(numGrid)



############################
#			Buttons		   #
############################

def Press(btn, x, y):
	btn["bg"] = "White"

def BombPress(btn, x, y):
	btn["bg"] = "blue"



#Show Maze With Labels 



def VisualizeMaze(grid=grid):
	ySize = len(grid)
	xSize = len(grid[0])

	btnGrid = []

	for y in range(xSize):
		row = []

		for x in range(ySize):
			if grid[x][y] == 0:
				btn = Button(root, bd=2, height=1, width=3, font=("calibri", 12, "bold"), bg="black",fg="white", text=int(numGrid[x,y]))
				btn.grid(row=x, column=y)
				row.append(btn)
				btn["command"] = lambda btn=btn, x=x, y=y: Press(btn, x, y)
			#show bomb location
			else:
				btn = Button(root, bd=2, height=1, width=3, font=("calibri", 12, "bold"), bg="red",fg="red")
				btn.grid(row=x, column=y)
				row.append(btn)
				btn["command"] = lambda btn=btn, x=x, y=y: BombPress(btn, x, y)
			
			
			
		btnGrid.append(row)

	return 

VisualizeMaze(grid)

mainloop()