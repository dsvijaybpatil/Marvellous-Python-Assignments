def Isprime(n):
    if n<=1:
        return False
    elif n==2 or n==3:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True
    



def main():
    data=list(map(int,input("Enter List:").split()))
    ans=list(filter(Isprime,data))
    print("Prime Numbers:",ans)

    
    
    

if __name__=="__main__":
    main()

