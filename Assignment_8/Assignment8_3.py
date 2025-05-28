import threading


def SumOfEven(value):
    sum1=0
    for i in value:
        if i%2==0:
            sum1=sum1+i
    print("Sum of Even Numbers in the List:",sum1)

def SumOfOdd(value):
    sum2=0
    for i in value:
        if i%2!=0:
            sum2=sum2+i
    print("Sum of Odd Numbers in the List:",sum2)
       
    
    


def main():
     numbers=input("Enter the five numbers:").split()
     data=[int(num) for num in numbers]
     T1=threading.Thread(target=SumOfEven,args=(data,))  
     T2=threading.Thread(target=SumOfOdd,args=(data,))  

     T1.start()
     T2.start()



if __name__=="__main__":
    main()