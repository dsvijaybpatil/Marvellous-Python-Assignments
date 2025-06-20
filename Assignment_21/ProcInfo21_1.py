import os
import sys
import psutil # type: ignore

def ProcessInfo():
    for proc in psutil.process_iter():
        info=proc.as_dict(attrs=['name',"pid","username"])
        print(info)

    
    
def main():
   Border="-"*80
   print(Border)
   print("-----------------------Marvellous Automation--------------------")
   print(Border)
   if (len(sys.argv)==1):
        if((sys.argv[0]=="--h") or sys.argv[0]=="--H"):
            print("This application is used to Display running Processess.")
            
        elif((sys.argv[0]=="--u") or sys.argv[0]=="--U"):
            print("Use the given script as")
            print("ScriptName.py")
            
        else:
            ProcessInfo()
            
   
   else:
        print("Invalid Number of Command line arguments.")         
        print("Use the given flag as:")
        print("--h: Use to Display the help.")
        print("--u: Use to Display the usage.")
       

if __name__=="__main__":
    main()