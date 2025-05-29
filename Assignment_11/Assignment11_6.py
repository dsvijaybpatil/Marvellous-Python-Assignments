sum=0
def SumOfN(no):
    global sum
    if(1<=no):
        sum=sum+no
        no=no-1
        SumOfN(no)
    return sum

def main():
    n=int(input("Enter the Number:"))
    ans=SumOfN(n)
    print("Sum of n Natural number is:",ans)



if __name__=="__main__":
    main()