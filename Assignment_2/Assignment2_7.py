def pattern():
    n=int(input("Entr the value:"))
    for i in range(n):
        for j in range(1,n+1):                
            print(j,end=" ")    # j will print its value from 1 to n       
        print()                 # it will go to the next row


if __name__=="__main__":
    pattern()
