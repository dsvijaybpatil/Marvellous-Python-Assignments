def AddAll():
    print("Enter number of elements:")
    size=int(input())

    Data=list()

    sum=0
    for i in range(size):
        no=int(input("Enter the values:"))
        Data.append(no)
        sum=sum+no                         # we add one by one elements of list in to the sum variable
    
    return sum                             # we return final sum of all elements of the list



if __name__=="__main__":
    print(AddAll())
