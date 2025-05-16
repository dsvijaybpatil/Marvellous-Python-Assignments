def Addfactors():
    n=int(input("Entr the Number:"))
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    return sum


if __name__=="__main__":
    print(Addfactors())
