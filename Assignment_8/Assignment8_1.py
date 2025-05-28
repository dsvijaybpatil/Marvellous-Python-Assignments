import threading

def Even():
    for i in range(2,21,2):
        print(i)

def Odd():
    for i in range(1,21,2):
        print(i)



def main():
    print("Inside main")
    T1=threading.Thread(target=Even)          # T1 Thread called to call back function Even will display first 10 even numbers
    T2=threading.Thread(target=Odd)          # T2 Thread called to call back function Odd will display first 10 odd numbers
                
    T1.start()
    T1.join()
    T2.start()
    

if __name__=="__main__":
    main()

