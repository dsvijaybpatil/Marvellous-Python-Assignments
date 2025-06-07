class Employee:
    def __init__(self,name,department,salary):
        self.name=name
        self._department=department
        self.__salary=salary
    def Display(self):
        print(self.__salary)

    
    


def main():
    obj1=Employee("Vijay","ES",35000)
    print(obj1.name)           #public variable we can acces throught object and class name anywhere within and outside class
    print(obj1._department)    #protected variable we can acces throught object and class name inside and outside class
    
    print(obj1.Display())      # private variable we can access within the class only   
    print(Employee.__salary)   # can't access outside the class showing attribute Error          

if __name__=="__main__":
    main()