class BankAccount:
    ROI=10.5
    Int=0
    def __init__(self,Name,Amount):
        self.Name=Name
        self.Amount=Amount
        
    
    def Diposit(self,DAmount):
        self.Amount=self.Amount+DAmount

    def Withdraw(self,WAmount):
         self.Amount=self.Amount-WAmount
        
    def CalculateIntrest(self):
         BankAccount.Int=(self.Amount*BankAccount.ROI)/100
         
    def Display(self):
         print("Name of the Account Holder is:",self.Name)
         print("Total Balance Amount is:",self.Amount)
         print("Total Interest as per ROI is",BankAccount.Int)

         
        
      
def main():
        Name= input("Enter the Name:")
        Amount1=int(input("Enter the Initial Amount:"))
        obj1=BankAccount(Name,Amount1)
        obj1.CalculateIntrest()
        obj1.Display()
        Amount2=int(input("Enter the Amount to Deposite:"))
        obj1.Diposit(Amount2)
        obj1.CalculateIntrest()
        obj1.Display()
        WAmount=int(input("Enter the Amount to Withdraw:"))
        obj1.Withdraw(WAmount)
        obj1.CalculateIntrest()
        obj1.Display()
        obj2=BankAccount("VIJAY",50000)
        obj2.CalculateIntrest()
        obj2.Display()
        obj2.Diposit(40000)
        obj2.CalculateIntrest()
        obj2.Display()
        obj2.Withdraw(30000)
        obj2.CalculateIntrest()
        obj2.Display()
if __name__=="__main__":
     main()

