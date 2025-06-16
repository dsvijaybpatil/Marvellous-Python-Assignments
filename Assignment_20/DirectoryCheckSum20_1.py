import os
import sys
import hashlib

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
    for folderName,subfolderNames,fileNames in os.walk(DirectoryName):
        for fname in fileNames:
            fname=os.path.join(folderName,fname)
            checksum=CalculateCheckSum(fname)
            print("The name of the file is:",fname)
            print("Check sum for the file is:",checksum)
    
def main():
   DirectoryWatcher(sys.argv[1])
       

if __name__=="__main__":
    main()