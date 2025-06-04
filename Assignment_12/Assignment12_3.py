class Arithmetic:
    
    def __init__(self):
        self.value1=0
        self.value2=0
        
    @classmethod
    def Accept(cls,x,y):
        cls.value1=x
        cls.value2=y
    
    
    def Addition(self):
        return Arithmetic.value1+Arithmetic.value2

    
    def Substraction(self):
        return Arithmetic.value1-Arithmetic.value2   

    def Multiplication(self):
         return Arithmetic.value1*Arithmetic.value2
    
    def Division(self):
         return Arithmetic.value1/Arithmetic.value2
         
        

      
def main():
        print("First Object output")
        obj1=Arithmetic()
        obj1.Accept(30,20)
        print(obj1.Addition())
        print(obj1.Substraction())
        print(obj1.Multiplication())
        print(obj1.Division())
        
        print("Second Object output")
        obj2=Arithmetic()
        obj2.Accept(15,20)
        print(obj2.Addition())
        print(obj2.Substraction())
        print(obj2.Multiplication())
        print(obj2.Division())
        
        print("Third Object output")
        obj3=Arithmetic()
        obj3.Accept(11,10)
        print(obj3.Addition())
        print(obj3.Substraction())
        print(obj3.Multiplication())
        print(obj3.Division())
        

if __name__=="__main__":
     main()

