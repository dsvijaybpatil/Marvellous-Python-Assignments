             
                      
                             

      
def main():
        obj=open("CleanFile.txt","a")
        
        for line in open("DATA.txt","r"):
           if not line.strip():
               continue 
           
           obj.write(line)

        obj.close()
        
        
        
        

if __name__=="__main__":
     main()

