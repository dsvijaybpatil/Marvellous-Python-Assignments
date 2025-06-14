import schedule
import time
import datetime

def LTime():
    print("Lunch Time!")

def WTime():
    print("Wrap of Work")
    
    
    
def main():
    
    schedule.every().day.at("01:00 PM").do(LTime)
    schedule.every().day.at("06:00 PM").do(WTime)

    

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()