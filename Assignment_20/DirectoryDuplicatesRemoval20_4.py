import os
import sys
import hashlib
import time

def CalculateCheckSum(path):
    fobj=open(path,"rb")

    hobj=hashlib.md5()
    buffer=fobj.read(1024)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer=fobj.read(1024)
    fobj.close()
    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName):
    flag=os.path.isabs(DirectoryName)   
    if flag==False:
        DirectoryName=os.path.abspath(DirectoryName)
    flag=os.path.exists(DirectoryName)
    if flag==False:
        print("The path is invalid.")
        exit()
    flag=os.path.isdir(DirectoryName)
    if flag==False:
        print("Path is valid but the target is invalid.")
        exit()
    Duplicate={}
    fobj=open("Log.txt","w")
    Border="*"*85
    for folderName,subfolderNames,fileNames in os.walk(DirectoryName):
        for fname in fileNames:
            fname=os.path.join(folderName,fname)
            checksum=CalculateCheckSum(fname)
            
            
            if(checksum in Duplicate):
                print('Name of Duplicate file is:'+fname)
                fobj.write(fname+"\n")
                os.remove(fname)
            else:
                Duplicate[checksum]=[fname]
    
    
def main():
   start=time.time()
   Border="-"*85
   print(Border)
   print("----------------------------------------------------------------")
   print("-----------------------Marvellous Automation--------------------")
   print("----------------------------------------------------------------")
   print(Border)
   if (len(sys.argv)==2):
        
        if((sys.argv[1]=="--h") or sys.argv[1]=="--H"):
            print("This application is used to perform Directory Cleaning.")
            print("This is the Directory automation script")
        elif((sys.argv[1]=="--u") or sys.argv[1]=="--U"):
            print("Use the given script as")
            print("ScriptName.py NameofDirectory")
            print("Please provide Absolute path")
        else:
            DirectoryWatcher(sys.argv[1])
   else:
        print("Invalid Number of Command line arguments.")         
        print("Use the given flag as:")
        print("--h: Use to Display the help.")
        print("--u: Use to Display the usage.")
   end=time.time()
   print("Time Required for the given script is:",end-start)
       

if __name__=="__main__":
    main()