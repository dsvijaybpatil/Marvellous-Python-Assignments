

def Display():
    n=int(input("Enter the number:"))
    count=0
    n=abs(n)                             # we convert negative number to positive to use the following logic
    while(n>=0):
        count+=1                         # we add 1 in count
        t=n//10                          # we reduce the size of number by one by using floor division of 10
        n=t
        if n==0:                         # once the value of n is zero we stop the loop
            break
    return count
                         


if __name__=="__main__":
    print(Display())

