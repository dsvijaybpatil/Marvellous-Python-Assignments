import os
   
def main():
   
   print("Enter the name of the file:")
   filename=input()
   print("Enter the string to search:")
   str=input()
   res=os.path.exists(filename)
   if res==True:
       print("File is exits in the current directory.")
       fobj=open(filename,'r')
       data=fobj.read()
       frq=data.count(str,0,len(data))
       print("Frequency of the given string is:",frq)
       
   else:
       print("File does not exit in the current direcory.")
       

if __name__=="__main__":
    main()