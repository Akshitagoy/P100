class Atm:
    def __init__(self,card,pin):
        self.card=card
        self.pin=pin
        

    def BalanceEnquiry(self):
        print("Your balance is :-")
        print("₹0.00")
      

    def CashWithdrawl(self,rupees):
        amount=0
        new_amount=amount-rupees
      
        print("You have withdrawn amount "+str(rupees) + ". Your remaining balance is "+ str(new_amount))

    def CashDeposit(self,rupees):
        amount=0
        new_amount=amount+rupees
      
        print("You have withdrawn amount "+str(rupees) + ". Your remaining balance is "+ str(new_amount))    
    
def main():
    print("Welcome to XYZ bank!🙏🏻")
    cardNumber = input("Please enter your card number:- ")
    pinNumber = input("Please enter your pin number:- ")  

    newUser=Atm(cardNumber,pinNumber)

    print("Choose one activity")
    print("1. Balance Enquiry 2. Cash Withdrawl or Cash deposit")  
    activity=int(input("Enter activity number:- "))

    if(activity == 1):
        newUser.BalanceEnquiry()
    elif(activity == 2):
        print("1. Cash Withdrawl 2.Cash Deposit")  
        activity2=int(input("Enter activity number:- "))
        if(activity2 == 1):
           rupees = int(input("Enter the amount to be withdrawn:- "))
           newUser.CashWithdrawl(rupees)
        elif(activity2 == 2):
            rupees = int(input("Enter the amount to be deposited:- "))
            newUser.CashDeposit(rupees)
        else:
            print("Enter valid activity number")
    else:
        print("Enter valid activity number")   

if __name__ == "__main__":
    main()



    

