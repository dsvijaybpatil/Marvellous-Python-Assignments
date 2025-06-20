import os
import sys
import psutil # type: ignore

def ProcessInfo(name):
    for proc in psutil.process_iter(["name"]):
        
        if proc.info["name"]==name:
            info=proc.as_dict(attrs=['name',"pid","username"])
            print(info)
        else:
            print("Process is not in Running Stage.")

    
    
def main():
   Border="-"*80
   print(Border)
   print("-----------------------Marvellous Automation--------------------")
   print(Border)
   if (len(sys.argv)==2):
        if((sys.argv[1]=="--h") or sys.argv[1]=="--H"):
            print("This application is used to Display given Processess.")
            
        elif((sys.argv[1]=="--u") or sys.argv[1]=="--U"):
            print("Use the given script as")
            print("ScriptName.py ProcessName")
            
        else:
            ProcessInfo(sys.argv[1])
            
   
   else:
        print("Invalid Number of Command line arguments.")         
        print("Use the given flag as:")
        print("--h: Use to Display the help.")
        print("--u: Use to Display the usage.")
       

if __name__=="__main__":
    main()