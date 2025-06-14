import os
def main():
    Filename="Student.txt"
    obj=open(Filename,"w")
    obj.write("Name of Student1, Name of Student2, Name of Student3, Name of the student4, Name of the Student5")
    obj.close()
    
    
if __name__=="__main__":
    main()
