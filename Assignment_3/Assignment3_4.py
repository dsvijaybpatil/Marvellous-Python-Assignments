def Frequency():
    print("Enter number of elements:")
    size=int(input())

    Data=list()

    
    for i in range(size):
        no=int(input("Enter the values:"))
        Data.append(no)
    print("Entered list elements are:",Data)
    search=int(input("Enter the element to search:"))
    count=0
    for j in Data:
        if search==j:
            count+=1
    return count                              



if __name__=="__main__":
    print(Frequency())
