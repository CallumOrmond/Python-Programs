from tkinter import *
#everything is a widget 

root = Tk() #First - Create Window Widget 

myLabel = Label(root, text="Hello World!") #Create Lable 
myLabe2 = Label(root, text="Hello World! Again!")
#myLabel.pack() #Put on screen - Anyway possible 


#Grid System
myLabel.grid(row=0,column=0)
myLabe2.grid(row=1,column=1)

#Create Event Loop - Window is always looping waiting for input (Refresh Rate)
root.mainloop() 



