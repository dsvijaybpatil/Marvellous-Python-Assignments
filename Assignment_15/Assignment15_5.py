import os
import sys
def main():
    Filename=input("Enter the Name of file:")
    str=input("Enter the String to Search:")

    ret=os.path.exists(Filename)

    if ret==True:
        print(Filename," is present in the current directory.")
        fobj1=open(Filename,"r")
        data=fobj1.read()
        frq=data.count(str,0,len(data))
        print("Frequency of the given string is:",frq)
        
    else:
        print(Filename,"is not present in the current directory.")
    
if __name__=="__main__":
    main()