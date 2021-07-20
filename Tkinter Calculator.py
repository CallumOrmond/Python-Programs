
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry("315x625")
root.title("Calculator")
root.configure(bg='black')

style = ttk.Style()
style.configure('W.TButton', font =
               ('calibri', 10, 'bold', 'underline'),
                foreground = 'red')

def ButtonPress(Key):
    global op
    op += str(Key)
    text.set(op)

def Clear():
    global op
    op = ""
    text.set("")



def Equals():
    global op
    if ")(" in op:
        op = op.replace(")(", ")*(")

    try:
        output = str(eval(op))
    except:
        text.set("INVALID ENTRY")

    op = ""
    text.set(output)


#GLOBALS
op = ""
text = tk.StringVar()


#TITLE + DISPLAY
DisplayLbl = tk.Label(root,fg="white", padx=16,pady=16,font=("calibri", 28, "bold"), bg="black", textvariable=text).grid(column=0,row=1, columnspan=4, sticky="E")

##BUTTON GRID##

#ROW 1
Clearbtn = tk.Button(root,padx=12,pady=12,bd=6,font=("calibri", 28, "bold"), bg="black",fg="white", text="C", command=Clear).grid(column=0,row=2)
LeftBracketBtn = tk.Button(root,padx=16,pady=12,bd=6,font=("calibri", 28, "bold"), bg="black",fg="white", text="(", command=lambda: ButtonPress("(")).grid(column=1,row=2)
RightBracketBtn = tk.Button(root,padx=16,pady=12,bd=6,font=("calibri", 28, "bold"), bg="black",fg="white", text=")", command=lambda: ButtonPress(")")).grid(column=2,row=2)

#OPERATION ON RIGHT SIDE
DivideBtn = tk.Button(root,padx=14,pady=12,bd=6,font=("calibri", 28, "bold"), bg="black",fg="white", text="/", command=lambda: ButtonPress("/")).grid(column=3,row=2)
MultiBtn = tk.Button(root,padx=12,pady=12,bd=6,font=("calibri", 28, "bold"), bg="black",fg="white", text="*", command=lambda: ButtonPress("*")).grid(column=3,row=3)
MinusBtn = tk.Button(root,padx=15,pady=12,bd=6,font=("calibri", 28, "bold"), bg="black",fg="white", text="-", command=lambda: ButtonPress("-")).grid(column=3,row=4)
AddBtn = tk.Button(root,padx=12,pady=12,bd=6,font=("calibri", 28, "bold"), bg="black",fg="white", text="+", command=lambda: ButtonPress("+")).grid(column=3,row=5)


#NUMBERS - ROW 2,3,4
Numbers = dict()
for i in range(0,3):
    Numbers["Button%s" %i] = tk.Button(root,padx=12,pady=12,bd=6,font=("calibri", 28, "bold"), bg="black",fg="white", text=str(i + 1), command=lambda i=i: ButtonPress(i + 1)).grid(column=i % 3,row=5)

for i in range(3,6):
    Numbers["Button%s" %i] = tk.Button(root,padx=12,pady=12,bd=6,font=("calibri", 28, "bold"), bg="black",fg="white", text=str(i + 1), command=lambda i=i: ButtonPress(i + 1)).grid(column=i % 3,row=4)

for i in range(6,9):
    Numbers["Button%s" %i] = tk.Button(root,padx=12,pady=12,bd=6,font=("calibri", 28, "bold"), bg="black",fg="white", text=str(i + 1), command=lambda i=i: ButtonPress(i + 1)).grid(column=i % 3,row=3)

#BOTTUM ROW 
Numbers["Button0"] = tk.Button(root,padx=12,pady=12,bd=6,font=("calibri", 28, "bold"), bg="black",fg="white", text=str(0), command=lambda: ButtonPress(0)).grid(column=0,row=6)
DecimalBtn = tk.Button(root,padx=16,pady=12,bd=6,font=("calibri", 28, "bold"), bg="black",fg="white", text=".", command=lambda: ButtonPress(".")).grid(column=1,row=6)
EqualsBtn = tk.Button(root,padx=52,pady=12,bd=6,font=("calibri", 28, "bold"), bg="black",fg="white", text="=", command=Equals).grid(column=2,row=6, columnspan=2)


root.mainloop()