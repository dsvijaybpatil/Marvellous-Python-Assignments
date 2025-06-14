def Displayfun(data):
       for x in data:
               count=0
               for i in x:
                      if i.isspace():
                             count+=1
               if count==5:
                      print(x)                   
                      
                      
                             

      
def main():
        obj=open("Data.txt","r")
        
        data=obj.readlines()
        Displayfun(data)
        
        obj.close()

if __name__=="__main__":
     main()

