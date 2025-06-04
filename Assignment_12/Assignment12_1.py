class Demo:
    value=0
    def __init__(self,no1,no2):
        self.no1=no1
        self.no2=no2
    
    def fun(self):
        print("Values from Fun method:")
        print(self.no1)
        print(self.no2)
    
    def gun(self):
        print("Values from Gun method:")
        print(self.no1)
        print(self.no2)

def main():
    value1=int(input("Enter the first Number:"))
    value2=int(input("Enter the first Number:"))
    Obj1=Demo(value1,value2)
    Obj2=Demo(value1,value2)
    Obj1.fun()
    Obj2.fun()
    Obj1.gun()
    Obj2.gun()  



if __name__=="__main__":
    main()