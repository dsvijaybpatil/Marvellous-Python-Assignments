def MinNumber():
    print("Enter number of elements:")
    size=int(input())

    Data=list()

    
    for i in range(size):
        no=int(input("Enter the values:"))
        Data.append(no)                           # we Add each element into the list
    print("Entered list elements are:",Data)
    
    min=Data[0]                         # we assign min element as first element of the list
    for j in Data:
        if min>j:                       # we check each element of the list for minimum
            min=j                        # we assign the min elemnt in to the min variable
    return min                              



if __name__=="__main__":
    print(MinNumber())
