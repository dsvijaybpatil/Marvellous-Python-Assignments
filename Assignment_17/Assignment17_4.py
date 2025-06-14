import schedule
import time
import datetime

def MySchedule():
    print("Namskar...")
    
    
    
def main():
    schedule.every().day.at("9:00 AM").do(MySchedule)

    

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()