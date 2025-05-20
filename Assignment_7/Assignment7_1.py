Square=lambda x:x**2

Cube=lambda x:x**3

def main():
    n=int(input("Enter the Number:"))
    ans1=Square(n)
    ans2=Cube(n)
    print("Square:",ans1)
    print("Cube:",ans2)

if __name__=="__main__":
    main()

