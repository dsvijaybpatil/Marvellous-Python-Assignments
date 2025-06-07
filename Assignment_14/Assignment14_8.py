class Vehicle:
    def start(self):
        print("We are Inside Vehicle start.")
class Car(Vehicle):
    def start(self):                         #overrided method
        print("We are Inside Car start.")

def main():
    obj1=Vehicle()
    obj2=Car()

    obj1.start()
    obj2.start()

if __name__=="__main__":
    main()