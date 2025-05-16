import MarvellousNum as mn

def ListPrime():
    print("Enter number of elements:")
    size=int(input())

    Data=list()

    
    for i in range(size):
        no=int(input("Enter the values:"))
        Data.append(no)
    print("Entered list elements are:",Data)
    
    sum=0
    for j in Data:
        chk=mn.ChkPrime(j)
        if chk:
            sum+=j
    return sum                              



if __name__=="__main__":
    print(ListPrime())
