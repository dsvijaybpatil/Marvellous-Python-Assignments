def Isprime(n):
    if n<2:
        return False
    elif n==2 or n==3:
        return True
    elif n%2==0 or n%3==0:
        return False
    i=5
    while(i*i<=n):
        if n%5==0 or n%(i+2)==0:
            return False
        i+=6
    return True
    


def main():
    n=int(input("Enter the value of Number:")) 
    res=Isprime(n)
    if res==True:
        print("{} is a Prime Number.".format(n))   
    else:
        print("{} is not Prime Number.".format(n))   



if __name__=="__main__":
    main()