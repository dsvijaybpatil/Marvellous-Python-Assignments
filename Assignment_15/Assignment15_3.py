import os
import sys
def main():
    Filename=sys.argv[1]

    ret=os.path.exists(Filename)

    if ret==True:
        print(Filename," is present in the current directory.")
        fobj1=open(Filename,"r")
        data=fobj1.read()
        fobj2=open("Demo.txt","w")
        fobj2.write(data)
        fobj2.close()
        fobj1.close()
        
    else:
        print(Filename,"is not present in the current directory.")
    
if __name__=="__main__":
    main()

