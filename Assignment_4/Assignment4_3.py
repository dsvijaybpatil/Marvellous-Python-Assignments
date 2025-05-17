

from functools import reduce
Check= lambda x:x>=70 and x<=90                # we check number lies between 70 and 90
    
Increse=lambda  x:x+10                         # we add 10 in each number

Product=lambda x,y:x*y                         # we take a product of two numbers

Data=[]
def main():
    size=int(input("Enter the size of list:"))       # we first size from user take 
    for i in range(size):
        no=int(input("Enter the element:"))
        Data.append(no)                            # we add each number into the list



if __name__=='__main__':
    main()
print("Input List is:",Data)
FData=list(filter(Check,Data))             # we first filter the data using filter and check lambda fuction
print("List after Filter:",FData)
MData=list(map(Increse,FData))             # we add 10 in each value of Fdata by using Increase lambda fuction
print('List after Map:',MData)
Rdata=reduce(Product,MData)                # we reduce data by taking cumulative product 
print("List after Reduce:",Rdata)
