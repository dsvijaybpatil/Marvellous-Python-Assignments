def IsPrime(no):
     if no<=1:
          return False
     elif no==2 or no==3:
          return True
     elif no%2==0 or no%3==0:
          return False
     i=5
     while(i*i<=no):
          if no%i==0 or no%(i+2)==0:
               return False
          i+=6
     return True
def MaxNum(no1,no2):
     if no1<=no2:
          return no2
     else:
          return no1           
def FilterX(Task,values):
      Result1=[]
      for x in values:
            res=Task(x)
            if res==True:
                  Result1.append(x)
      return Result1

def MapX(values):
     Result2=[]
     for x in values:
          Result2.append(2*x)
     return Result2

def ReduceX(Task,values):
     Result3=0
     for x in values:
          Result3=Task(Result3,x)
     return Result3



def main():
    l=input("Enter the list:").split()
    data=[int(x) for x in l]
    print(data,type(data))
    Fdata=FilterX(IsPrime,data)
    print("List after filter is:",Fdata)
    Mdata=MapX(Fdata)
    print("List after Map is:",Mdata)
    Ans=ReduceX(MaxNum,Mdata)
    print("Output of Reduce is:",Ans)



    

if __name__=="__main__":
    main()

