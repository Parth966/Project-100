class atm:
    def __init__(self,pinNumber, cardNumber):
            self.pinNumber = pinNumber
            self.cardNumber = cardNumber
            
    def balanceEnquiry(self):
       print("Current balance is $5000") 

    def cashWithdrawal(self,amount):
       new_amount = 5000-amount
       print(new_amount)
     

def main():
    cardNumber = input("Please enter your card number")  
    pinNumber = input("Please eanter your pin number")
    newUser = atm(cardNumber,pinNumber)
    print("Choose option 1 or option 2")
    print("1 - Check your balance")
    print("2 - Cash withdrawal")
    activity = int(input("Please enter the number of your chosen option"))
    if (activity == 1):
        newUser.balanceEnquiry()
    elif (activity == 2):
        amount = int(input("Enter amount here"))
        newUser.cashWithdrawal(amount)    

main()        