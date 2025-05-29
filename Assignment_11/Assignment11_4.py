power=1
def PowerFun(no1,no2):
    global power
    if(1<=no2):
        power=power*no1
        no2=no2-1
        PowerFun(no1,no2)
    return power

def main():
    n=int(input("Enter the first Number:"))
    m=int(input("Enter the second Number:"))

    ans=PowerFun(n,m)
    print("Power of n upto m Number is:",ans)



if __name__=="__main__":
    main()