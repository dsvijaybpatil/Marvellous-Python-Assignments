def Pattern1(n):
    print("Pattern using For loop.")
    for i in range(1,n+1):
        for j in range(i):
            print("*",end=" ")
        print()
    
def Pattern2(n):
    print("Pattern using While loop.")
    i=1
    while(i<=n):
            j=1
            while(j<=i):
                 print("*",end=" ")
                 j+=1
            print()
            i+=1

def main():
    n=int(input("Enter the value of Number:")) 
    Pattern1(n)
    Pattern2(n)  



if __name__=="__main__":
    main()