import os
import sys
    
    
def main():
   
   res=os.path.exists(sys.argv[1])
   if res==True:
       print("File is exit in the current directory.")
       fobj=open(sys.argv[1],"r")
       data=fobj.read()
       fobj1=open("Demo.txt","w")
       print('Data is copied into Demo.txt file.')
       fobj1.write(data)
       fobj1.close()
       fobj.close()
   else:
       print("File does not exit in the current direcory.")
       

if __name__=="__main__":
    main()