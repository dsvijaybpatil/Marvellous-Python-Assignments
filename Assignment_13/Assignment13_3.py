class Numbers:
    
    def __init__(self,Value):
        self.Value=Value
           
    
    def ChkPrime(self):
        if(self.Value<=1):
             return False
        elif self.Value==2 or self.Value==3:
             return True
        elif (self.Value)%2==0 or (self.Value)%3==0:
             return False
        else:
             for i in range(4,self.Value):
                  if (self.Value)%i==0:
                       return False
        return True
    
    def Factors(self):
         self.sum=0
         for i in range(1,self.Value+1):
              if self.Value%i==0:
                   print(i,end=",")
                   self.sum=self.sum+i
         print()
    def ChkPerfect(self):
         if (self.sum-self.Value)==self.Value:
              return True
         else:
              return False
        
    def SumFactors(self):
         print("Sum of the Factors are:",self.sum)

    
         
    

         
        
      
def main():
        x=int(input("Enter the Value:"))
        obj1=Numbers(x)
        ret=obj1.ChkPrime()
        print(ret)
        obj1.Factors()
        obj1.SumFactors()
        print(obj1.ChkPerfect())
        print("For second object created:")
        obj2=Numbers(6)
        ret1=obj2.ChkPrime()
        print(ret1)
        obj2.Factors()
        obj2.SumFactors()
        print(obj2.ChkPerfect())
if __name__=="__main__":
     main()

