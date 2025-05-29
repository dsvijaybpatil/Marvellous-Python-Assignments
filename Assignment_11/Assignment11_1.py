i=1
def PrintNumbers(no):
    global i
    if(i<=no):
        print(i,end=" ")
        i+=1
        PrintNumbers(no)

def main():
    n=int(input("Enter the Number:"))
    PrintNumbers(n)



if __name__=="__main__":
    main()