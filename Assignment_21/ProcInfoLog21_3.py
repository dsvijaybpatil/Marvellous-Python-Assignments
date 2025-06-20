import os
import sys
import psutil # type: ignore

def ProcessInfo(FolderName):
    flag=os.path.isabs(FolderName)
    if flag==False:
        FolderName=os.path.abspath(FolderName)
        print(FolderName)
    flag=os.path.exists(FolderName)
    print(flag)
    if flag==False:
        print("The given directory does not exists.")
        exit()
    flag=os.path.isdir(FolderName)
    if flag==False:
        print("The given path is correct but it is not a directory.")
    

    for proc in psutil.process_iter():       
        
            info=proc.as_dict(attrs=['name',"pid","username"])
            obj=open(os.path.join(FolderName,"Logfile.log"),"a")
            obj.write(str(info))
            
            
       
        

    
    
def main():
   Border="-"*80
   print(Border)
   print("-----------------------Marvellous Automation--------------------")
   print(Border)
   if (len(sys.argv)==2):
        if((sys.argv[1]=="--h") or sys.argv[1]=="--H"):
            print("This application is used to stored Processess in log file.")
            
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