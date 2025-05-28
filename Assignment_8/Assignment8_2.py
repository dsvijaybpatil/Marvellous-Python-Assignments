import threading

def SumEvenFactors(n):
    sum1=0
    for i in range(2,n+1,2):
        if n%i==0:
            sum1=sum1+i
    print("Sum of Even Factors:",sum1)

def SumOddFactors(n):
    sum2=0
    for i in range(1,n+1,2):
        if n%i==0:
            sum2=sum2+i
    print("Sum of Odd Factors:",sum2)

        



def main():
    print("Inside main")
    n=int(input("Enter the Number:"))
    T1=threading.Thread(target=SumEvenFactors,args=(n,))          # T1 Thread called to sum of all even factors of number
    T2=threading.Thread(target=SumOddFactors,args=(n,))          # T2 Thread called to sum of all odd factors of number
                
    T1.start()
    T1.join()
    T2.start()
    T2.join()
    print("Exit from main")
    

if __name__=="__main__":
    main()

