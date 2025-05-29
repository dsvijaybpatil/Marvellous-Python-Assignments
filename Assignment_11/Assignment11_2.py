fact=1
def Factorial(no):
    global fact
    if(1<=no):
        fact=fact*no
        no=no-1
        Factorial(no)
    return fact

def main():
    n=int(input("Enter the Number:"))
    ans=Factorial(n)
    print("Factorial of the given Number is:",ans)



if __name__=="__main__":
    main()