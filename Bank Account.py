#To create the BankAccount class
class bank:
   def __init__(self):
   
      self.bal=0 #Intialize balance to 0
      print("Welcome to the SBI")

   def deposit(self):
       amt=float(input("Enter amount to be Deposited:"))
       
      self.bal+=amt
      print("\n deposited amount :", amt)
    
   def Withdraw(self):
       amt=float(input("Enter amount to be Withdraw:"))
       
     if self.bal>=amt:
      self.bal-=amt
      print("\nYou Withdraw:", amt)
     else:
      print("\nInsufficient balance")

   def display(self):
      print("\nNet Available Balance=",self.bal)

#driver code
if __name__== "__main__":
   s=bank() #create an object ofBankAccount
   s.deposite()   #Deposite money
   s.Withdraw()    #Withdraw money
   s.display()    #Display balance
