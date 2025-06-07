class Rectangle:
    
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
        
    def Display(self):
        area=(self.length)*(self.width)
        perimeter=2*(self.length+self.width)
        print("Area of Rectangle is:",area)
        print("Perimeter of the Rectangle is:",perimeter)
      
def main():
        obj1=Rectangle(10,5)
        obj1.Display()
        
if __name__=="__main__":
     main()

