from tkinter import * 
import random
import time

root = Tk()
Size = 25
#############################
# Setup for Maze            #
#############################

#Create 2D Array to store maze

def MakeEmptyGrid(Size):
	grid = []
	for i in range(Size):
		row = []
		for j in range(Size):
			row.append(0)
		grid.append(row)

	return grid

grid = MakeEmptyGrid(Size)

#Show Maze With Labels 

def VisualizeMaze(grid=grid):
	ySize = len(grid)
	xSize = len(grid[0])

	btnGrid = []

	for x in range(xSize):
		column = []

		for y in range(ySize):
			if grid[y][x] == 0:
				lbl = Label(root, bg="white", padx=7, pady=0, borderwidth=1, relief="solid")
			else:
				lbl = Label(root, bg="black", padx=7, pady=0, borderwidth=1, relief="solid")
			lbl.grid(row=y, column=x)
			column.append(lbl)
		btnGrid.append(column)

	return 

def CreateMaze(grid, Size):
	x = 0 
	y = 0

	for i in range(Size):
		for j in range(Size):
			
			value = random.randint(0,3)
			valueAgain = random.randint(0,8)
			print(value)

			if valueAgain == 0:
				if value == 0 and y < Size:
					y = y + 1
				if value == 1 and y >= 0:
					y = y - 1
				if value == 2 and x < Size:
					x = x + 1
				if value == 3 and x >= 0:
					x = x - 1

			grid[y][x] = 1

				

CreateMaze(grid, Size)
VisualizeMaze(grid)

mainloop()