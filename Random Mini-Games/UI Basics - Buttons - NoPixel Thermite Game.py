#Python3
from tkinter import *

import tkinter
import random
import time
from datetime import datetime

root = Tk() 
#GAME STATE - Replay does not work
#ADDITIONS  - Size Change in game, timer change in game 
#HOW IT WORKS - Start = Start the game

#Base Params 
active="#ffffff" #clicked - white
default_color="#07363b" #default - blue
Size=6
D=[]
Pattern = []
FalseCounter = 0 
GameActive = False
StartTime = False

TimerLabel = Label(root, text=3)
TimerLabel.grid(row=Size+1, column=2)

def main(D=D,height=Size,width=Size):

  for x in range(width):
    for y in range(height):
      btn = tkinter.Button(root, bg=default_color, padx=15, pady=8,activebackground = default_color)
      btn.grid(column=x, row=y)
      D.append([False, btn.configure, str(x) + str(y),])
      
      #Can't have funtion with parameters in btn creation
      #so add lamda funtion which is the funtion with params 

      #lambda (params/variables) : logic (call funtion/ params + 10/ etc.)
      #Can do x = lambda then to call do x(a,b) which returns logic 
      btn["command"] = lambda btn=btn, x=x, y=y: click(btn,x,y)
  BntStrat = Button(root, command=Start, text="Start")
  BntStrat.grid(row=height+1,column=1)

  return 

#randomly pick squres 
def Start(D=D,Size=Size + 3,active=active,default_color=default_color,Pattern=Pattern):
  global GameActive
  global StartTime

  if GameActive == False:
    GameActive = None
    #White Square Selection + Colour Change
    random.shuffle(D)
    for i in range(Size - 1):
      D[i][1](bg=active)
      Pattern.append(D[i][2])

    #Timer
    for i in range(3):
      TimerLabel.configure(text=3-i)
      root.update()
      time.sleep(1)
    TimerLabel.configure(text=0) 
    StartTime = time.time()
    


    #Set back to default Colour 
    for i in range(Size):
      D[i][1](bg=default_color)
      D[i][0] = True

    #Start Game 
    GameActive = True
  return

#click colour change
def click(button,x,y):
  global GameActive
  global FalseCounter

  if GameActive == True:
    if str(x) + str(y) in Pattern:

      Pattern.remove(str(x) + str(y))
      button["bg"] = active

      if len(Pattern) == 0:
        GameActive = False
        GameOver("Winner!")
      
    else:
      button["bg"] = "red"
      FalseCounter = FalseCounter + 1
      if FalseCounter >= 3:    
        GameActive = False
        GameOver("Failed")
      
#Scuffed - Replay does not work     
def GameOver(result):

  def Replay():
    newWindow.destroy()
    main()
    return

  global StartTime
  if result == "Winner!":
    Time = str(round(time.time() - StartTime , 2)) + "s"
    result = "Winner! in " + Time

  newWindow = Toplevel(root) 
  newWindow.title(result)
  newWindow.geometry("150x50")
  Label(newWindow, text=result).pack() 
  btn = Button(newWindow, text="Play Again?", command=Replay).pack()

main(D,Size,Size)
tkinter.mainloop()