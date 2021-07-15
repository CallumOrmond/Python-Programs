#Banking App
#Withdraw and Deposit
#Write each tansaction in file 

class Bank:

    def __init__(self, Money):
        self.Money = Money

    def WithDraw(self, amount):
        if amount > 0:
            self.Money = self.Money - amount
            NoteTransaction(amount, "withdrawn")
            print("You have", self.Money, "remaining")


    def Deposit(self, amount):
        if amount > 0:
            self.Money = self.Money + amount
            NoteTransaction(amount, "deposited")
            print("You have", self.Money, "remaining")

    def Balance(self):
        print("You have", self.Money, "remaining")

def NoteTransaction(amount, action):
    f = open("SS - Advanced Python (Python 301) - Classes/BankTransactions.txt", "a")       
    f.write(str(amount) + " was " + str(action) + " from you account \n")  
    f.close()

account = Bank(1000)

while True:
    action = input("What would you like to do, W = Withdraw | D = Deposit | B = Balance - ")
    if action.lower() in ["w", "d", "b", "exit"]:
        if action == "w":
            amount = input("How much would you like to withdraw - ")

            try:
                amount = int(amount)
            except:
                amount = 0
                print("Invalid - Input has to be number")
            account.WithDraw(amount)

        elif action == "d":
            amount = input("How much would you like to deposit - ")
            try:
                amount = int(amount)         
            except:
                amount = 0
                print("Invalid - Input has to be number")
            account.Deposit(amount)

        elif action == "b":
            account.Balance()
        
        elif action == "exit":
            break
    else:
        print("This is not a valid option - to leave type exit")

            