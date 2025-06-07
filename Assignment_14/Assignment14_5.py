class bankAccount:
        
    def __init__(self,name,account_no,balance=0):
        self.account_no=account_no
        self.name=name
        self.balance=balance
    def Deposite(self,Amount):
         self.balance=self.balance+Amount
        
    def Withdraw(self,withdraw):
         if(self.balance>=withdraw):
              self.balance=self.balance-withdraw
         elif(self.balance<withdraw):
              print("Insufficient Balance")
              print("Thank for Banking with us.")
         else:
              print("Enter the valid Amount.")   
      
        
    def Display(self):
        print("Name of Account Holder is:",self.name)
        print("Account Number is:",self.account_no)
        print("Total Balance is:",self.balance)
        
    
            
    
def main():
        Name=input("Enter the Name:")
        Number=int(input("Enter the Account Number:"))
        obj1=bankAccount(Name,Number)
        Amount=int(input("Ente the Amount to Depoiste:"))
        obj1.Deposite(Amount)        
        obj1.Display()    
        Amount=int(input("Ente the Amount to withdraw:"))        
        obj1.Withdraw(Amount)        
        obj1.Display()    
        
        obj2=bankAccount("Vijay Patil",15545)
        obj2.Display()    
        Amount=int(input("Ente the Amount to Depoiste:"))
        obj2.Deposite(Amount)        
        obj2.Display()    
        Amount=int(input("Ente the Amount to withdraw:"))        
        obj2.Withdraw(Amount)        
        obj2.Display()    
          
         
        
if __name__=="__main__":
     main()

