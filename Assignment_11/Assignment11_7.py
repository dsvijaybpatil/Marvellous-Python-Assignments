i=1
def Pattern(no):
    global i
    if(i<=no):
        for x in range(i):
            print("*",end=" ")
        i+=1
        
        print()
        Pattern(no)
        
    return sum

def main():
    n=int(input("Enter the Number:"))
    ans=Pattern(n)
    



if __name__=="__main__":
    main()