import schedule
import time
import datetime

def BackUp():
    
    fobj=open("Filename.txt","r")
    data=fobj.read()
    fobj1=open("Back_up.txt","w")
    fobj1.write(data)

    fobj.close()
    fobj1.close()



    
    
def main():
    
    schedule.every(1).hour.do(BackUp)
        

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()