class Person:
        
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Display2(self):
        print("Name of the Person is: "+self.name)
        print("Age of the Person is:",self.age)

class Teacher(Person):
     def __init__(self,subject,salary,name,age):
          self.subject=subject
          self.salary=salary
          self.name=name
          self.age=40
     
     def Display1(self):
          print("Subject name is:",self.subject)
          print("Salary is:",self.salary)
          super().__init__(self.name,self.age)
def main():
     obj1=Teacher("English",50000,"Vijay",40)
     obj1.Display1()
     obj1.Display2()
        
if __name__=="__main__":
     main()

