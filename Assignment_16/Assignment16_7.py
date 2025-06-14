def Display(data):
       data1=[]
       data2={}
       for x in data:
               x.replace(":","")
               data1.append(x)
       
       for y in data1:
               z=y.split(":")
               
               data2[z[0]]=int(z[1])
               if int(z[1])>=75:
                      print(z[0])               
                      
            
def main():
        
        obj=open("marks.txt","r")
        fdata=obj.readlines()
        data=[]
        for x in fdata:
               z=x.replace("\n","")
               data.append(z)
        Display(data)     
        
        
        
     
        obj.close()
if __name__=="__main__":
     main()

