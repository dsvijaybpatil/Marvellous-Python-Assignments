class Book:
    
    def __init__(self):
        self.__price=0
        
        
        
    def set(self,price):
        self.__price=price
        
    def get(self):
        print("Book Price is:",self.__price)
            
    
def main():
        obj1=Book()
        obj1.set(2000)          # we set Book price
        obj1.get()              # we get Book price
         
        
if __name__=="__main__":
     main()

