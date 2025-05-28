import threading
import time

def Dislay():
    for i in range(1,6):
        print(i)





def main():
    print("Inside main")
    
    thread1=threading.Thread(target=Dislay)          
    thread2=threading.Thread(target=Dislay) 
    thread3=threading.Thread(target=Dislay)    
                
    thread1.start()
    thread1.join()
    time.sleep(1)
    thread2.start()
    thread2.join()
    time.sleep(1)
    thread3.start()

    

if __name__=="__main__":
    main()

