import os
import sys

def Check():
    obj1=open(sys.argv[1],"r")
    data1=obj1.read()
    obj2=open(sys.argv[2],"r")
    data2=obj2.read()
    if data1==data2:
        print("Success")
    else:
        print("Failure")
    
def main():
    ret1=os.path.exists(sys.argv[1])
    ret2=os.path.exists(sys.argv[2])
    if ret1==True and ret2==True:
        print("Both the Files are exits in the Directory")
        Check()

    else:
        print("either both or one of the File are not exit in the Directory")
    
    
if __name__=="__main__":
    main()

