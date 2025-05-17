

from functools import reduce
CheckEven= lambda x:x%2==0                  # we check number is even if divisible by 2
    
Square=lambda  x:x**2                        # we take square of each number

Addition=lambda x,y:x+y                     # cumulatively we add all numbers

Data=[]
def main():
    size=int(input("Enter the size of list:"))
    for i in range(size):
        no=int(input("Enter the element:"))
        Data.append(no)                         # we add each number into the list



if __name__=='__main__':
    main()
print("Input List is:",Data)
FData=list(filter(CheckEven,Data))             # we first filter the data using filter and checkEven lambda fuction
print("List after Filter:",FData)
MData=list(map(Square,FData))             # we add 10 in each value of Fdata by using Square lambda fuction
print('List after Map:',MData)
Rdata=reduce(Addition,MData)                # we reduce data by taking cumulative addition
print("List after Reduce:",Rdata)
