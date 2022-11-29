
##########   VISULISATION   ##########       
            

import sys
import pygame

# CONSTANTS:
SCREENSIZE = WIDTH, HEIGHT = 1100, 1100
BLACK = (0, 0, 0)
GREY = (160, 160, 160)
WHITE = (255, 255, 255)
PADDING = PADTOPBOTTOM, PADLEFTRIGHT = 50, 50
# VARS:
_VARS = {'surf': False}


def main(state):
    pygame.init()
    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    _VARS['surf'].fill(WHITE)
    

    # state = [[0,11,15,4], [0,0,15,11], [0, 0, 6, 11]]

    ScreenSize = 1000
    n = 10
    ratio = 1000 / n

    drawSquare(0, 0, n, n, ratio, n)

    
    for rec in state:
        drawSquare(rec[0], rec[1], rec[0] + rec[2], rec[1] + rec[3], ratio, n, True)


    while True:
        checkEvents()
        pygame.display.update()


def drawSquare(x1, y1, x2, y2, ratio, n, first=False):

    x1 = x1 * ratio
    x2 = x2 * ratio
    y1 = (n - y1) * ratio
    y2 = (n - y2) * ratio

    #draw bottum
    drawRect((x1, y1), (x2, y1))

    #draw right wall
    drawRect((x2, y1), (x2, y2))

    #draw top 
    drawRect((x2, y2), (x1, y2))

    #draw left wall
    drawRect((x1, y2), (x1, y1))

    if first:
        #draw cross to show square
        drawRect((x1, y1), (x2, y2), 1)
        drawRect((x1, y2), (x2, y1), 1)




def drawRect(start, end, pen=5):
    
    start

    pygame.draw.line(
      _VARS['surf'], BLACK,
      (start[0] + PADLEFTRIGHT, start[1] + PADTOPBOTTOM),
      (end[0] + PADLEFTRIGHT, end[1] + PADTOPBOTTOM), pen)
   


def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
      
















##########   COMPUTATION ##########



def splitx(state, square, x):
 
    newstate = state.copy()
    newstate.remove(square)
    
    new1 = square.copy()
    new2 = square.copy()

    new1[2] = x

    new2[0] = new2[0] + x
    new2[2] = square[2] - x

    newstate.append(new1)
    newstate.append(new2)

    if check(newstate) == True:
        return newstate
    else:
        print("-----   Invalid   ---")
        return False

def splity(state, square, y):
	newstate = state.copy()
	newstate.remove(square)
    
	new1 = square.copy()
	new2 = square.copy()

	new1[3] = y

	new2[1] = new2[1] + y
	new2[3] = square[3] - y

	newstate.append(new1)
	newstate.append(new2)

	if check(newstate) == True:
		return newstate
	else:
		print("-----   Invalid   ---")
	return False

def check(state):
    result = checkDimensions(state) and checkOverlaps(state)
    if not result:
        print("Check Fail")
    return result


def checkDimensions(state):

    L = []
    # check no rectangles are the same
    for rectangle in state:
        Rsize1 = (rectangle[2], rectangle[3])
        Rsize2 = (rectangle[3], rectangle[2])
        if Rsize1 in L or Rsize2 in L:
            print("False - Dimensions match", Rsize1, Rsize2)
            return False
        else:
            L.append(Rsize1)
            L.append(Rsize2)

    print("Valid Dimensions")
    return True


def is_overlapping_1D(line1, line2):
    return line1[0] < line2[1] and line2[0] < line1[1]

def is_overlapping_2d(box1, box2):
    return is_overlapping_1D([box1[0],box1[2]],[box2[0],box2[2]]) and is_overlapping_1D([box1[1],box1[3]],[box2[1],box2[3]])

def checkOverlaps(state):

    for tile in state:
        for otherTile in state:
            if (tile != otherTile):
                box1 = [tile[0], tile[1], tile[0] + tile[2], tile[1] + tile[3]]
                box2 = [otherTile[0], otherTile[1], otherTile[0] + otherTile[2], otherTile[1] + otherTile[3]]
                if (is_overlapping_2d(box1, box2)):
    
                    print("False - Overlap")
                    print(tile, otherTile)
            
                    return False

    print("No Overlaps")
    return True



def checkNewDimension(state, dimension=(0,0)):
    L = []
    # check no rectangles are the same
    for rectangle in state:
        Rsize1 = (rectangle[2], rectangle[3])
        Rsize2 = (rectangle[3], rectangle[2])
    
    if dimension in L:
        print("Dimension in Square")
        return False
		
    return True


def cost(state):
	MinArea = 1000000
	MaxArea = 0

	for tile in state:
		area = tile[2] * tile[3]

		if area < MinArea:
			MinArea = area
		if area > MaxArea:
			MaxArea = area

	score = MaxArea - MinArea
	return score


def biggestTile(state):
	MaxArea = 0
	maxtile = []

	for tile in state:
		area = tile[2] * tile[3]

		if area > MaxArea:
			MaxArea = area
			maxtile = tile

	return maxtile

# a = size of sqare, M = limiting factor 
def SolveMondrian(a, M):

	# make inital square with dinmesions a
	state = []
	state.append([0, 0, a, a])

	# state = [[0, 8, 15, 7], [0, 0, 8, 8], [8, 0, 7, 8]]
	bestState = []
	bestStateScore = 100000

	for i in range(M):
		maxtile = biggestTile(state)

		if maxtile[2] > maxtile[3]:
			#larger x than y - split x 
			xSplit = round(maxtile[2]/2)

			while not splitx(state, maxtile, xSplit):
				xSplit = xSplit - 1
				if xSplit < 0:
					break

			state = splitx(state, maxtile, xSplit)

		else:
			#larger y than x - split y 
			ySplit = round(maxtile[3]/2)

			while not splity(state, maxtile, ySplit):
				ySplit = ySplit - 1
				if ySplit < 0:
					break

			state = splity(state, maxtile, ySplit)

		
		score = cost(state)
		if score < bestStateScore:
			bestState = state
			bestStateScore = score

	print("Score :", bestStateScore)
	return bestState

    
state = SolveMondrian(10, 6)

# state = [[0,11,15,4],[0,0,15,11]]
# state = splitx(state, [0,0,15,11], 7)
# state = splity(state, [0,11,15,4], 2)

print(state)

if state != False:
    checkDimensions(state)
    checkOverlaps(state)




main(state)




               