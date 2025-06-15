import os
import sys


def Checkdata(data1,data2):
    if data1==data2:
        print("Success")  
    else:
        print("Failure") 
    
def main():
   
   res1=os.path.exists(sys.argv[1])  
   res2=os.path.exists(sys.argv[2])
   if res1==True and res2==True:
       print("both the Files are exit in the current directory.")
       fobj1=open(sys.argv[1],"rb")
       data1=fobj1.read()
       
       fobj2=open(sys.argv[2],"rb")
       data2=fobj2.read()
       
       Checkdata(data1,data2)


       fobj1.close()
       fobj2.close()
   else:
       print("Either both the Files or one of the file does not exit in the current direcory.")
       

if __name__=="__main__":
    main()