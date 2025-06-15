import os
    
    
def main():
   print('Enter the Name of file:')
   filename=input()
   res=os.path.exists(filename)
   if res==True:
       print("File is exit in the current directory.")
   else:
       print("File does not exit in the current direcory.")
       

if __name__=="__main__":
    main()