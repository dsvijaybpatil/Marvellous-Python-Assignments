def factorial():
    n=int(input("Entr the value:"))
    if n<0:
        print("Enter the positive number only")
        return False
    elif n==0:
        return 1
    else:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
    return fact


if __name__=="__main__":
    print(factorial())
