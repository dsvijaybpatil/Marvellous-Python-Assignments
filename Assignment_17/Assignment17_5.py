import schedule
import time
import datetime

def MySchedule():
    data=time.ctime()
    obj=open("Marvellous.txt","a")
    
    obj.write(data+"\n")
    
    
    
def main():
    schedule.every(5).minutes.do(MySchedule)

    

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()