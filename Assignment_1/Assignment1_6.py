def ChkNum(x):
    if x==0:
        print("Zero")
    elif(x<0):
        print("Negative Number")
    else:
        print("Positive Number")

def Display():
    print("Enter the number:")
    a=int(input())
    ChkNum(a)


if __name__=="__main__":
    Display()
