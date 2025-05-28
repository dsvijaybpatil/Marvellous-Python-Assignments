import threading


def CountofSmall(str):
    sum1=0
    print("Id of the current thread is:",threading.get_native_id())
    print("Name of the current thread is:",threading.current_thread())
    for i in str:
        if i.islower():
            sum1+=1
    print("Small Characters in the String:",sum1)

def CountofCaital(str):
    print("Id of the current thread is:",threading.get_native_id())
    print("Name of the current thread is:",threading.current_thread())

    sum2=0
    for i in str:
        if i.isupper():
            sum2+=1
    print("Capital Characters in the String:",sum2) 

def CountofDigit(str):
    print("Id of the current thread is:",threading.get_native_id())
    print("Name of the current thread is:",threading.current_thread())

    sum3=0
    for i in str:
        if i.isdigit():
            sum3+=1
    print("Number of digits in the String:",sum3)       
    
    


def main():
     str=input("Enter the given String:")
     Small=threading.Thread(target=CountofSmall,args=(str,))
     Capital=threading.Thread(target=CountofCaital,args=(str,))
     Digits=threading.Thread(target=CountofDigit,args=(str,))  
    
     Small.start()
     Small.join()
     Capital.start()
     Capital.join()
     Digits.start()



if __name__=="__main__":
    main()