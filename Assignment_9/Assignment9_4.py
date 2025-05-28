import threading
import multiprocessing
import time


def SumofNumbers():
    sum=0
    for i in range(1,10000001):
        sum=sum+i
    print("Sum of 10 Million:",sum)


def main():
     start1=time.time()
     SumofNumbers()
     end1=time.time()
     print("Time required by using Normal function is:",end1-start1)
     T1=threading.Thread(target=SumofNumbers)
     start2=time.time()
     T1.start()
     T1.join()
     end2=time.time()
     print("Time required by using threading is:",end2-start2)
     M1=multiprocessing.Process(target=SumofNumbers)
     start3=time.time()
     M1.start()     
     M1.join()
     end3=time.time()
     print("Time required by using multiprocessing is:",end3-start3)


    
if __name__=="__main__":
    main()