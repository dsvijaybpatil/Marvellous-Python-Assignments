class Circle:
    PI=3.14
    def __init__(self):
        self.Radius=0
        self.Area=0
        self.Circumference=0
    @classmethod
    def Accept(cls,R):
        cls.Radius=R
    
    @classmethod
    def CalculateArea(cls):
        cls.Area=Circle.PI*Circle.Radius*Circle.Radius

    @classmethod
    def CalculateCircumference(cls):
        cls.Circumference=2*Circle.PI*Circle.Radius
        

   
        

    @staticmethod
    def Display():
        print("Radius of Circle is:",Circle.Radius)
        print("Area of Circle is:",Circle.Area)
        print("Circumference of Circle is:",Circle.Circumference)
        
def main():
        Radius=int(input("Enter the Radius of Circle:"))
        obj1=Circle()
        obj1.Accept(Radius)
        obj1.CalculateArea()
        obj1.CalculateCircumference()
        Circle.Display()
        obj2=Circle()
        obj2.Accept(5)
        obj2.CalculateArea()
        obj2.CalculateCircumference()
        Circle.Display()
        obj3=Circle()
        obj3.Accept(11)
        obj3.CalculateArea()
        obj3.CalculateCircumference()
        Circle.Display()

if __name__=="__main__":
     main()

