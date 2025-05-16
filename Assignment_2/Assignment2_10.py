

def Display():
    n=int(input("Enter the number:"))
    sum=0
    n=abs(n)                 # we convert negative number to positive to use following code            
    while n:
        p=n%10               # we find the last digit of given number
        sum=sum+p                         # we add every time last digit in sum
        n//=10                          # we reduce the size of number by one by using floor division of 10
        
    return sum
                         


if __name__=="__main__":
    print(Display())

