def ChkNum(x):
    if x%5==0:            
        return True
    else:
        return False

def Display():
    print("Enter the number:")
    a=int(input())
    print(ChkNum(a))


if __name__=="__main__":
    Display()
