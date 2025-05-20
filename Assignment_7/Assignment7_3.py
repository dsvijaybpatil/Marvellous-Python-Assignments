Even=lambda x:x%2==0



def main():
    data=list(map(int,input("Enter List:").split()))
    ans1=list(filter(Even,data))
    
    print("Even Numbers:",ans1)
    

if __name__=="__main__":
    main()

