

def Display():
    print("Enter the number:")
    n=int(input())
    for i in range(n,0,-1):
        for j in range(i):            # * will display first n times then n-1 times,n-2times,.. and so on
            print("*",end=" ")
        print()                       # it will shift to the next row


if __name__=="__main__":
    Display()
