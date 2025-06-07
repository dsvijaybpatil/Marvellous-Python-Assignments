class Employee:
    NoOfBooks=0
    def __init__(self,Name,emp_id,salary):
        self.Name=Name
        self.emp_id=emp_id
        self.salary=salary
        
    def Display(self):
        print("Name:",self.Name,"ID:",self.emp_id,"Salary:",self.salary)
      
def main():
        obj1=Employee("Rohit",101,5000)
        obj1.Display()
        
if __name__=="__main__":
     main()

