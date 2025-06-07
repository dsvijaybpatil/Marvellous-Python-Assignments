class Student:
    school_name="Mahatma"
    
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        
        
        
    def Display(self):
        print("Student Name is:",self.name)
        print("Id is:",self.roll_no)
        print("Name of school is:",Student.school_name)
        
    
            
    
def main():
        obj1=Student("vijay",2025)
        obj1.Display() 
        Student.school_name="Carmel"  # we change the name of school using class name
        obj1.Display()        
         
        
if __name__=="__main__":
     main()

