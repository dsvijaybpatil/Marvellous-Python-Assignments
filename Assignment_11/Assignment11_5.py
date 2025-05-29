count=0
def CountZeros(no):
    global count
    if(1<=no):
        if(no%10==0):
            count+=1
        no=no//10
        CountZeros(no)
    return count

def main():
    n=int(input("Enter the Number:"))
    ans=CountZeros(n)
    print("Number of zeros in the given Number is:",ans)



if __name__=="__main__":
    main()