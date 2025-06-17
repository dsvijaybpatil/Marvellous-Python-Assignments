import os
import sys
import shutil

def DirectoryCopy(FolderName,NewFolderName,Extention):
    flag=os.path.isabs(FolderName)
    if flag==False:
        FolderName=os.path.abspath(FolderName)
    flag=os.path.exists(FolderName)
    if flag==False:
        print("Given Directory does not exists.")
        exit()
    flag=os.path.isdir(FolderName)
    if flag==False:
        print('The given path is correct but file is not directory.')
        exit()
    os.mkdir(NewFolderName)
    for FolderName,subfolderName,FileNames in os.walk(FolderName):
        for fname in FileNames:
                fname=os.path.join(FolderName,fname)
                if fname.endswith(Extention):
                    shutil.copy(fname,NewFolderName)
                
                
    
    
def main():
   Border="-"*80
   print(Border)
   print("-----------------------Marvellous Automation--------------------")
   print(Border)
   if (len(sys.argv)==2):
        if((sys.argv[1]=="--h") or sys.argv[1]=="--H"):
            print("This application is used to copy given Extention file from one Directory to another Directory. ")
            
        elif((sys.argv[1]=="--u") or sys.argv[1]=="--U"):
            print("Use the given script as")
            print("ScriptName.py NameofDirectory NameofNewDirectory .Extention")
            
        else:
            print("Invalid Number of Command line arguments.") 
            print("Use the given flag as:")
            print("--h: Use to Display the help.")
            print("--u: Use to Display the usage.")
   elif (len(sys.argv)==4):
       DirectoryCopy(sys.argv[1],sys.argv[2],sys.argv[3])
   else:
        print("Invalid Number of Command line arguments.")         
        print("Use the given flag as:")
        print("--h: Use to Display the help.")
        print("--u: Use to Display the usage.")
       

if __name__=="__main__":
    main()