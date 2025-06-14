def CountCfun(data):
       ccount=0
       for x in data:
               
               for i in x:
                      if i.isspace():
                             continue
                      else:
                             ccount+=1
       print("The number of characters in the file are:",ccount)                    
                      
                      
                             
def CountWfun(data):
       wcount=0
       for x in data:
               
               for i in x:
                      if i.isspace():
                             wcount+=1
       print("The number of words in the file are:",wcount)
      
def main():
        obj=open("Data.txt","r")
        
        data=obj.readlines()
        n=len(data)
        print("The total numbers of lines in the given file:",n)
        CountWfun(data)
        CountCfun(data)
        obj.close()

if __name__=="__main__":
     main()

