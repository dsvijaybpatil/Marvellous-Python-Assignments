def TableOfN(n):
    i=1
    while(i<=10):
        print(n,"X",i,"=",i*n)            
        i+=1
def main():
    n=int(input("Enter the value of N:")) 
    TableOfN(n)   

if __name__=="__main__":
    main()