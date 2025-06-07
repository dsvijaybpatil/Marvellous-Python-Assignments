class Calculator:
        
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def Add(self):
         print("Addition of two nubers are:",self.a+self.b)
    def Subtract(self):
         print("Subtraction of two nubers are:",self.a-self.b)
    def Muliply(self):
         print("Multiplication of two nubers are:",self.a*self.b) 
    def Divide(self):
         print("Division of two nubers are:",self.a/self.b)    

def main():
        a=int(input("Enter the first nuber:"))
        b=int(input("Enter the first nuber:"))
        obj1=Calculator(a,b)

        m=int(input("Enter the number of method you will execute."))
        for x in range(m):
             n=int(input("Enter 1=Additio 2=substraction 3=multiplication 4=division: "))
             if(n==1):
                  obj1.Add() 
             elif(n==2):
                  obj1.Subtract()
             elif(n==3):
                  obj1.Muliply() 
             elif(n==4):
                  obj1.Divide()        
         
        
if __name__=="__main__":
     main()

