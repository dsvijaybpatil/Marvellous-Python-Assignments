
      
def main():
        obj1=open("source.txt","r")
        data=obj1.read()
        obj2=open("Destination.txt","a")
        obj2.write(data)

        obj1.close()
        obj2.close()
if __name__=="__main__":
     main()

