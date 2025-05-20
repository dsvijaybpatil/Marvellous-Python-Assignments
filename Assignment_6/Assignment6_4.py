def FactOfN(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("Factorial of {} is:{}".format(n,fact))
    


def main():
    n=int(input("Enter the value of Number:")) 
    FactOfN(n)  



if __name__=="__main__":
    main()