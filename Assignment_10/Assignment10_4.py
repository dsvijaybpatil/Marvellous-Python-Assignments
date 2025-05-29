Even=lambda x:x%2==0
Square=lambda x:x**2
Add=lambda x,y:x+y
            
def FilterX(Task,values):
      Result1=[]
      for x in values:
            res=Task(x)
            if res==True:
                  Result1.append(x)
      return Result1

def MapX(Task,values):
     Result2=[]
     for x in values:
          Result2.append(Task(x))
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
    Fdata=FilterX(Even,data)
    print("List after filter is:",Fdata)
    Mdata=MapX(Square,Fdata)
    print("List after Map is:",Mdata)
    Ans=ReduceX(Add,Mdata)
    print("Output of Reduce is:",Ans)



    

if __name__=="__main__":
    main()

