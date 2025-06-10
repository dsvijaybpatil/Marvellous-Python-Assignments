import os
def main():
    print("Enter the name of the file:")
    Filename=input()

    ret=os.path.exists(Filename)

    if ret==True:
        print(Filename," is present in the current directory.")
        fobj=open(Filename,"r")
        data=fobj.read()
        print('Content of the File is:',data)
        fobj.close()

        
    else:
        print(Filename,"is not present in the current directory.")
    
if __name__=="__main__":
    main()

