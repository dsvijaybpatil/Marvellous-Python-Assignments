sum=0
def SumOfDigits(no):
    global sum
    if(1<=no):
        sum=sum+no%10
        no=no//10
        SumOfDigits(no)
    return sum

def main():
    n=int(input("Enter the Number:"))
    ans=SumOfDigits(n)
    print("Sum of digits of the given Number is:",ans)



if __name__=="__main__":
    main()