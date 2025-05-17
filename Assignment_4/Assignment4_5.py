

from functools import reduce

def filterX(Task,Values):
    Result=[]
    for no in Values:
        ret=Isprime(no)            # we cheeck for number prime
        if ret==True:
            Result.append(no)        # if prime then we append into the list
    return Result
                 
    
Multiply=lambda  x:x*2                        # we multiply each number by 2

Max =lambda x,y:x<y
def ReduceX(Task,Values):
    Result=0
    for no in Values:
        ret=Task(Result,no)
        if ret==True:
            Result=no
    return Result                    # cumulatively we add all numbers

def Isprime(n):                      # function to check number is prime or not
    if n<=1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while(i*i<=n):
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True

Data=[]
def main():
    size=int(input("Enter the size of list:"))
    for i in range(size):
        no=int(input("Enter the element:"))
        Data.append(no)                         # we add each number into the list



if __name__=='__main__':
    main()
print("Input List is:",Data)
FData=list(filterX(Isprime,Data))                    # we first filter the data using filter and ChecPrime number fuction
print("List after Filter:",FData)
MData=list(map(Multiply,FData))             # we multyply each value by 2 of Fdata by using Multiply lambda fuction
print('List after Map:',MData)
Rdata=ReduceX(Max,MData)                # we find the maximum number from the list
print("List after Reduce:",Rdata)
