
import tkinter as tk
import random 



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

        for F in (HomePage, MathsPage, TimesTablesTimed): #Frames 

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
        EnglishZoneBtn = tk.Button(self, text="Click For English").grid(row=2,column=0)
        MoreBtn = tk.Button(self, text="Test Area").grid(row=3,column=0)


class MathsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Maths Zone!").pack()

        Maths_Multiplication = tk.Button(self, text="Times Tables", command=lambda: controller.show_frame(TimesTablesTimed)).pack()
        BackBtn = tk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage)).pack()
       

class TimesTablesTimed(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        #Variables
        self.TimesTable = 1
        self.sum = tk.StringVar()
        self.score = 0
        self.answer = -1
        self.timerCount = 10

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

        self.StartBtn = tk.Button(self, text="Start", command=self.Start)
        self.StartBtn.grid(row=3,column=1)
        
        self.CurrentMultiLbl = tk.Label(self, text="Current Times Table: " + str(self.TimesTable))
        self.CurrentMultiLbl.grid(row=3,column=2)

        controller.bind('<Return>', self.Enter)

    #Called by Number buttons 
    def UpdateMulti(self, val):
        self.TimesTable = val
        self.CurrentMultiLbl.configure(text="Current Times Table: " + str(self.TimesTable))


    #Called on Start Button
    def Start(self):
        if self.timerCount == 10:                           #Start Timer
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
                self.ScoreLbl.configure(text="Score: " + str(self.score))

                self.CreateSum()
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
        self.sum.set(str(self.TimesTable) + " * " + str(rnd))
        self.answer = eval(self.sum.get())


   



app = main()
app.mainloop()