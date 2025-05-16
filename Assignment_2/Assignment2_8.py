

def Display():
    n=int(input("Enter the number:"))
    
    for i in range(1,n+1):
        for j in range(1,i+1):            
            print(j,end=" ")           # value of j will be display 1 then next row 1 2 then 1 2 3 so on ...
        print()                       # it will shift to the next row


if __name__=="__main__":
    Display()
