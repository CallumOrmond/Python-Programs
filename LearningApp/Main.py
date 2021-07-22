
import tkinter as tk
import random 
import time



class main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack()

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.title("App")
        self.geometry("1000x1000")

        self.frames = dict()

        for F in (HomePage, MathsPage, TimesTablesTimed, TimesTablesStreak, EnglishPage, TypingMatch): #Frames 

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()




class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        lable = tk.Label(self, text="Welcome to the Fun Zone!").grid(row=0,column=0)

        MathsZoneBtn = tk.Button(self, text="Click For Maths", command=lambda: controller.show_frame(MathsPage)).grid(row=1,column=0)
        EnglishZoneBtn = tk.Button(self, text="Click For English", command=lambda: controller.show_frame(EnglishPage)).grid(row=2,column=0)
        MoreBtn = tk.Button(self, text="Test Area").grid(row=3,column=0)

class MathsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="English Zone!").pack()

        English_Typing = tk.Button(self, text="Times Tables", command=lambda: controller.show_frame(TimesTablesTimed)).pack()
        Maths_Multiplication_Streak = tk.Button(self, text="Times Table - Streak", command=lambda:controller.show_frame(TimesTablesStreak)).pack()
        BackBtn = tk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage)).pack()

class EnglishPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Maths Zone!").pack()

        Maths_Multiplication = tk.Button(self, text="Typing Game", command=lambda: controller.show_frame(TypingMatch)).pack()
        BackBtn = tk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage)).pack()
       

class TypingMatch(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        #Variables
        self.pos = 0
        self.Start = False
        self.t = 0
        self.TEXT_OPTIONS = ["Test rhis is a long text to show"]
        self.textLen = 0

        self.startTime = 0
        self.endTime = 0

        #Buttons
        TextTestLbl = tk.Label(self, text="")

        self.text = tk.Text(self, font=("calibri", 18, "bold"))
        self.text.grid()

        self.text.insert("end", "testing text - this is for testing poggers C")
        self.text.configure(state="disable")

        self.ResetBtn = tk.Button(self, text="Click for New text", command=self.Reset)
        self.ResetBtn.grid()

        
        #Setup
        self.text.tag_add("Setup", "0.0 + " + str(self.pos) + " chars")
        self.text.tag_configure("Setup", background="light green")


        #EXIT BUTTON
        BackBtn = tk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage)).grid()
        controller.bind('<KeyPress>', self.Keyboard)


    def Reset(self):
        self.Start = True
        self.pos = 0
        
        self.t = random.choice(self.TEXT_OPTIONS)
        self.textLen = len(self.t)

        self.text.configure(state="normal")
        self.text.delete("0.0", "end")
        self.text.insert("end", self.t)
        self.text.configure(state="disable")


    def Keyboard(self, event):
        if self.Start == True:
            
            self.StartTime = time.time()

            if event.keysym == "BackSpace" or event.keysym == "Shift_L":
                pass
            else:      

                Character = self.text.get("0.0 + " + str(self.pos) + " chars", "0.0 + " + str(self.pos + 1) + " chars")       
                if event.char == Character:
                    
                    self.text.tag_add("Prevouis Text",  "0.0 + " + str(self.pos) + " chars")
                    self.text.tag_configure("Prevouis Text", foreground="grey")

                    self.text.tag_add("current", "0.0 + " + str(self.pos + 1) + " chars")
                    self.text.tag_configure("current", background="light green")

                    self.text.tag_add("currentRemove", "0.0 + " + str(self.pos) + " chars")
                    self.text.tag_configure("currentRemove", background="white")

                    self.pos += 1

                    if self.pos == self.textLen:
                        print("REACHED END")
                        self.text.tag_add("currentRemove", "0.0 + " + str(self.pos) + " chars")
                        self.text.tag_configure("currentRemove", background="white")
                        self.endTime = time.time()
                        print(self.endTime , self.startTime, self.endTime - self.StartTime)
                        self.Start = False

       
 



class TimesTablesTimed(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        #Variables
        self.TimesTable = 1
        self.sum = tk.StringVar()
        self.score = 0
        self.answer = -1
        self.timerCount = 25
        self.ranNum = 0

        #Create Buttons
        TimesTablesButtons = dict()
        for i in range(10):
            TimesTablesButtons["Button%s" %i] = tk.Button(
                self, text=str(i + 1), command=lambda i=i: self.UpdateMulti(str(i + 1))
            )
            TimesTablesButtons["Button%s" %i].grid(row=i + 1, column=0)

        #text="Press Start and enter the answer to the sum, get as many as you can before the timer reaches 0, good luck"
        self.Titlelbl = tk.Label(self, text="Press Start")
        self.Titlelbl.grid(row=0,column=1)

        self.SumDisplayLbl = tk.Label(self, textvariable=self.sum)
        self.SumDisplayLbl.grid(row=1,column=1)

        self.TimerLbl = tk.Label(self, text="Time Left: " + str(self.timerCount))
        self.TimerLbl.grid(row=1,column=2)

        self.UserAnswerBox = tk.Entry(self)
        self.UserAnswerBox.grid(row=2,column=1)

        self.ScoreLbl = tk.Label(self, text="Score: " + str(self.score))
        self.ScoreLbl.grid(row=2,column=2)

        self.StartBtn = tk.Button(self, text="Start", command=lambda:self.Start(controller))
        self.StartBtn.grid(row=3,column=1)

        self.CorrectOrWrongLbl = tk.Label(self)
        self.CorrectOrWrongLbl.grid(row=4,column=1)
        
        self.CurrentMultiLbl = tk.Label(self, text="Current Times Table: " + str(self.TimesTable))
        self.CurrentMultiLbl.grid(row=3,column=2)

        #EXIT BUTTON
        BackBtn = tk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage)).grid()


    #Called by Number buttons 
    def UpdateMulti(self, val):
        self.TimesTable = val
        self.CurrentMultiLbl.configure(text="Current Times Table: " + str(self.TimesTable))


    #Called on Start Button
    def Start(self, controller):
        controller.bind('<Return>', self.Enter)
        if self.timerCount == 25:                           #Start Timer
            self.Timer()

        self.ScoreLbl.configure(text="Score: " + str(self.score))
        self.UserAnswerBox.configure(state="normal")
        self.StartBtn.configure(state="disabled")
        self.UserAnswerBox.focus_set()
        self.CreateSum()
        
    #Called when user presses enter
    def Enter(self, event):
        if self.timerCount > 0:                                #Checks Timer
            if self.UserAnswerBox.get() == str(self.answer):    #Check Answer
                self.score += 1
                self.CorrectOrWrongLbl.configure(text="Correct!")
                self.ScoreLbl.configure(text="Score: " + str(self.score))

                self.CreateSum()
            else:
                self.CorrectOrWrongLbl.configure(text="Wrong!")
        self.UserAnswerBox.delete(0, "end")

    #Called From Start Method -Start Timer
    def Timer(self):
        if self.timerCount > 0:                         
            self.timerCount -= 1
            self.TimerLbl.configure(text="Time Left: " + str(self.timerCount))
            self.TimerLbl.after(1000, self.Timer)
        else:                                           #RESET after game
            self.StartBtn.configure(state="normal")
            self.UserAnswerBox.configure(state="disabled")
            self.UserAnswerBox.delete(0, "end")
            self.timerCount = 10
            self.answer = -1
            self.score = 0


    #Create New Sum
    def CreateSum(self):

        rnd = random.randint(1,10)
        while rnd == self.ranNum:
            rnd = random.randint(1,10)
        self.ranNum = rnd

        self.sum.set(str(self.TimesTable) + " * " + str(rnd))
        self.answer = eval(self.sum.get())


   
class TimesTablesStreak(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        #Variables
        self.TimesTable = 1
        self.sum = tk.StringVar()
        self.score = 0
        self.answer = -1
        self.ranNum = 0

        #Create Buttons
        TimesTablesButtons = dict()
        for i in range(10):
            TimesTablesButtons["Button%s" %i] = tk.Button(
                self, text=str(i + 1), command=lambda i=i: self.UpdateMulti(str(i + 1))
            )
            TimesTablesButtons["Button%s" %i].grid(row=i + 1, column=0)

        #text="Press Start and enter the answer to the sum, get as many as you can before the timer reaches 0, good luck"
        self.Titlelbl = tk.Label(self, text="Press Start")
        self.Titlelbl.grid(row=0,column=1)

        self.SumDisplayLbl = tk.Label(self, textvariable=self.sum)
        self.SumDisplayLbl.grid(row=1,column=1)

        self.UserAnswerBox = tk.Entry(self)
        self.UserAnswerBox.grid(row=2,column=1)

        self.ScoreLbl = tk.Label(self, text="Score: " + str(self.score))
        self.ScoreLbl.grid(row=2,column=2)

        self.StartBtn = tk.Button(self, text="Start", command=lambda:self.Start(controller))
        self.StartBtn.grid(row=3,column=1)

        self.CorrectOrWrongLbl = tk.Label(self)
        self.CorrectOrWrongLbl.grid(row=4,column=1)
        
        self.CurrentMultiLbl = tk.Label(self, text="Current Times Table: " + str(self.TimesTable))
        self.CurrentMultiLbl.grid(row=3,column=2)

        #EXIT BUTTON
        BackBtn = tk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage)).grid()

        

    #Called by Number buttons 
    def UpdateMulti(self, val):
        self.TimesTable = val
        self.CurrentMultiLbl.configure(text="Current Times Table: " + str(self.TimesTable))


    #Called on Start Button
    def Start(self, controller):
        controller.bind('<Return>', self.Enter)

        self.ScoreLbl.configure(text="Score: " + str(self.score))
        self.UserAnswerBox.configure(state="normal")
        self.StartBtn.configure(state="disabled")
        self.UserAnswerBox.focus_set()
        self.CorrectOrWrongLbl.configure(text="")
        self.CreateSum()
        
    #Called when user presses enter
    def Enter(self, event):
                                       
        if self.UserAnswerBox.get() == str(self.answer):    #Check Answer
            self.score += 1
            self.CorrectOrWrongLbl.configure(text="Correct!")
            self.ScoreLbl.configure(text="Score: " + str(self.score))

            self.CreateSum()
        else:
            self.CorrectOrWrongLbl.configure(text="Wrong!")
            self.end()

        self.UserAnswerBox.delete(0, "end")

    def end(self):
        self.StartBtn.configure(state="normal")
        self.UserAnswerBox.configure(state="disabled")
        self.UserAnswerBox.delete(0, "end")
        self.answer = -1
        self.score = 0

      #Create New Sum
    def CreateSum(self):

        rnd = random.randint(1,10)
        while rnd == self.ranNum:
            rnd = random.randint(1,10)
        self.ranNum = rnd

        self.sum.set(str(self.TimesTable) + " * " + str(rnd))
        self.answer = eval(self.sum.get())


    



app = main()
app.mainloop()