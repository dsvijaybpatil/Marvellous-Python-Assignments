from functools import reduce

Product=lambda x,y:x*y



def main():
    data=list(map(int,input("Enter List:").split()))
    ans1=reduce(Product,data)
    
    print("Product:",ans1)
    

if __name__=="__main__":
    main()

