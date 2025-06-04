class BookStore:
    NoOfBooks=0
    def __init__(self,Name,Author):
        self.Name=Name
        self.Author=Author
        self.Circumference=0
        BookStore.NoOfBooks+=1
    
    def Display(self):
        print(self.Name,"by",self.Author+". No of Books:",BookStore.NoOfBooks)
      
def main():
        obj1=BookStore("Linux System Programming","Robert Love")
        obj1.Display()
        obj2=BookStore("C Programming","Dennis Ritchie")
        obj2.Display()
        obj3=BookStore("Python Programming","Kanetkar")
        obj3.Display()
if __name__=="__main__":
     main()

