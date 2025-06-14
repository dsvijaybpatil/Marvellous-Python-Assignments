
      
def main():
        obj=open("Numbers.txt","w")
        for i in range(10):
               number=input("Enter the number:")
                   
               obj.write(number+"\n")
        obj.close()
if __name__=="__main__":
     main()

