def MaxElement():
    print("Enter number of elements:")
    size=int(input())

    Data=list()

    
    max=0
    for i in range(size):
        no=int(input("Enter the values:"))
        Data.append(no)
        if max<no:                         # we check the entered number is greater than max variable then we assign it into max element
            max=no
    
    return max                             # final we return maximum element



if __name__=="__main__":
    print(MaxElement())
