Double=lambda x:x*2



def main():
    data=list(map(int,input("Enter List:").split()))
    ans1=list(map(Double,data))
    
    print("Doubled List:",ans1)
    

if __name__=="__main__":
    main()

