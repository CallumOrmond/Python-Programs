
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


global RecSizeN

def main(state):
    pygame.init()
    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    _VARS['surf'].fill(WHITE)
    

    # state = [[0,11,15,4], [0,0,15,11], [0, 0, 6, 11]]

    ScreenSize = 1000
    n = RecSizeN
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

    if check(newstate, new1, new2) == True:
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

    if check(newstate, new1, new2) == True:
        return newstate
    else:
        print("-----   Invalid   ---")
    return False

def check(state, new1, new2):
    result = checkDimensions(state) and checkOverlaps(state) and checkNewDimension(state, new1) and checkNewDimension(state, new2)
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



def checkNewDimension(state, rec):
    L = []

    dimension = (rec[2], rec[3])

    if rec[2] <= 0 or rec[3] <= 0:
        print("Dimension too small")
        return False

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

def smallestTile(state):
	MinArea = 100000
	mintile = []

	for tile in state:
		area = tile[2] * tile[3]

		if area < MinArea:
			MinArea = area
			mintile = tile

	return mintile


def canMerge(state, tile):
    
    for rec in state:
        if rec != tile:
            if rec[0] == tile[0] and rec[3] == tile[3]:
                # can merge by removing horizontal line 
                newDimension = (0, 0, rec[2], rec[3] + tile[3])
                if checkNewDimension(state, newDimension):
                    #valid to merge
                    return (rec, tile)

            elif rec[1] == tile[1] and rec[3] == tile[3]:
                # can merge by removing vertical line 
                newDimension = (0, 0, rec[2] + tile[3], rec[3])
                if checkNewDimension(state, newDimension):
                    #valid to merge
                    return (rec, tile)

    return False

def Merge(state, tile):
    
    biggestTileS = biggestTile(state)
    biggestArea = biggestTileS[2] * biggestTileS[3]

    print("Merge Tile -", tile)

    for rec in state:
        if rec != tile and rec != biggestTileS:
            if rec[0] == tile[0] and rec[2] == tile[2] and (((tile[1] + tile[3] == rec[1])) or ((rec[1] + rec[3]) == tile[1])):
                # can merge by removing horizontal line 

                print("Merge x ")
                newDimension = (0, 0, rec[2], rec[3] + tile[3])
                newArea = newDimension[2] * newDimension[3]
                if newArea <= biggestArea or True:
                    if checkNewDimension(state, newDimension):
                        #valid to merge
                        state = xMerge(state, rec, tile)
                        return state
                    else:
                        print("dem wrong x")

            if rec[1] == tile[1] and rec[3] == tile[3] and (((tile[0] + tile[2]) == rec[0]) or ((rec[0] + rec[2]) == tile[0])):
                # can merge by removing vertical line 

                print("Merge y ")
                newDimension = (0, 0, rec[2] + tile[2], rec[3])
                newArea = newDimension[2] * newDimension[3]
                if newArea <= biggestArea or True:
                    if checkNewDimension(state, newDimension):
                        #valid to merge
                        state = yMerge(state, rec, tile)
                        return state
                    else:
                        print("dem wrong y")

    print("cant Merge")
    return False


def xMerge(state, tile1, tile2):

    newstate = state.copy()
    newstate.remove(tile1)
    newstate.remove(tile2)

    new1 = tile1.copy()
    
    # new1[0] same
    new1[1] = min(tile1[1], tile2[1])
    # new1[2] same
    new1[3] = tile1[3] + tile2[3]

    newstate.append(new1)

    print(tile1, tile2, new1)
    print(state)

    return newstate

def yMerge(state, tile1, tile2):

    newstate = state.copy()
    newstate.remove(tile1)
    newstate.remove(tile2)

    new1 = tile1.copy()
    
    new1[0] = min(tile1[0], tile2[0])
    # new1[1] same
    new1[2] = tile1[2] + tile2[2]
    # new1[3] same

    newstate.append(new1)

    print(tile1, tile2, new1)
    print(state)

    return newstate







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
        mintile = smallestTile(state)

        maxArea = maxtile[2] * maxtile[3]
        minArea = mintile[2] * mintile[3]

        print(maxArea, (minArea * 2))
        if maxArea < (minArea * 3) or i == 0:

            ### Split ###maxArea > (minArea * 2)
            move = 0
            changed = False

            xSplit = round(maxtile[2]/2)
            ySplit = round(maxtile[3]/2)

            print(maxtile, xSplit, ySplit)

            if xSplit > ySplit:
                #larger x than y - split x 
                
                while not splitx(state, maxtile, xSplit):
                    xSplit = xSplit - 1
                    print("xSplit", xSplit)
                    if xSplit <= 0:
                        break
                
                if (xSplit > 0):
                    state = splitx(state, maxtile, xSplit)
                    changed = True

            else:
                #larger y than x - split y 
                print("Here", splity(state, maxtile, ySplit))
                while not splity(state, maxtile, ySplit):
                    ySplit = ySplit - 1
                    print("ySplit", ySplit)
                    if ySplit <= 0:
                        break
                
                if (ySplit > 0):
                    state = splity(state, maxtile, ySplit)
                    changed = True


            score = cost(state)
            if score < bestStateScore:
                bestState = state
                bestStateScore = score

    else:

        ### Merge ###
        if Merge(state, smallestTile(state)) != False:
            state = Merge(state, smallestTile(state))

        score = cost(state)
        if score < bestStateScore:
            bestState = state
            bestStateScore = score

    ### end ### 

        
    score = cost(state)

    print("Best Score :", bestStateScore)
    print("Current Score :", score)

    return state

RecSizeN = 12

state = SolveMondrian(RecSizeN, 100)

# state = [[0,11,15,4],[0,0,15,11]]
# state = splitx(state, [0,0,15,11], 7)
# state = splity(state, [0,11,15,4], 2)


print("Here")


print("Final State:", state)

if state != False:
    checkDimensions(state)
    checkOverlaps(state)


main(state)



# approach 2 - more random 


### Working middle

#           if xSplit > ySplit:
#             #larger x than y - split x 
#                 xSplit = round(maxtile[2]/2)

#                 while not splitx(state, maxtile, xSplit):
#                     xSplit = xSplit - 1
#                     print("xSplit", xSplit)
#                     if xSplit <= 0:
#                     break
                
#                 if (xSplit > 0):
#                     state = splitx(state, maxtile, xSplit)
#                     changed = True

#             else:
#                 #larger y than x - split y 
#                 ySplit = round(maxtile[3]/2)

#                 while not splity(state, maxtile, ySplit):
#                     ySplit = ySplit - 1
#                     print("ySplit", ySplit)
#                     if ySplit <= 0:
#                         break
                
#                 if (ySplit > 0):
#                     state = splity(state, maxtile, ySplit)
#                     changed = True



   
    # for i in range(M):
    #     # sort based on area
    #     state.sort(key= lambda x: x[2] * x[3])

    #     maxtile = state[-1 - move]
    #     print("MAXTILE :", maxtile, move)

    #     changed = False

    #     xSplit = round(maxtile[2]/2)
    #     ySplit = round(maxtile[3]/2)

    #     Valid = False

    #     while not Valid:

    #         print(xSplit, ySplit)

    #         if xSplit > ySplit:
    #         #larger x than y - split x       
    #             if xSplit > 1:   
    #                 xSplit = xSplit - 1
    #             if splitx(state, maxtile, xSplit) != False:
    #                 Valid = True
    #         else:
    #             #larger y than x - split y 
    #             if ySplit > 1:                    
    #                 ySplit = ySplit - 1
    #             if splity(state, maxtile, xSplit) != False:
    #                 Valid = True
                

    #         if xSplit <= 1 and ySplit <= 1:
    #             break

    #     if (splitx(state, maxtile, xSplit) != False):
    #         state = splitx(state, maxtile, xSplit)
    #         changed = True
    #         move = 0
    #     elif (splity(state, maxtile, ySplit) != False):
    #         state = splity(state, maxtile, ySplit)
    #         changed = True
    #         move = 0


    #     if changed == False:
    #         move = move + 1
    #         if move > len(state) - 1:
    #             break
    


    # canMergeFlag = True
    # while  canMergeFlag != False:

    #     t = smallestTile(state)
    #     canMergeFlag = Merge(state, t)
    #     if canMergeFlag != False:
    #         state = Merge(state, t)
            
               