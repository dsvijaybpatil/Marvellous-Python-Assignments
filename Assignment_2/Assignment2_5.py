def Isprime(n):
    if n<2:
        return False
    elif n==2 or n==3 or n==5:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True

def main():
    n=int(input("Enter the number:"))
    result=Isprime(n)
    if result==True:
        print("The given number is prime.")
    else:
        print("The given number is not prime.")








if __name__=="__main__":
    main()