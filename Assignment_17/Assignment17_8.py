import schedule
import time
import datetime

def Check():
    
    print("checking mail...")



    
    
def main():
    
    schedule.every(10).seconds.do(Check)
        

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()