def Add(x,y):
    z=x+y
    return z

def Display():
    print("Enter the first number:")
    a=int(input())
    print("Enter the second number:")
    b=int(input())
    t=Add(a,b)
    print("The addition of two numbers is:",t)


if __name__=="__main__":
    Display()
