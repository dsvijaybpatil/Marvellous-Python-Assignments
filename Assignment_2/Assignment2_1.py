import Arithmetic as arm
def main():
    a=int(input("Enter the first_value:"))
    b=int(input("Enter the second_value:"))
    print("Addition is:",arm.Add(a,b))
    print("Substraction is:",arm.Sub(a,b))
    print("Multiplication is:",arm.Mult(a,b))
    print("Division is:",arm.Div(a,b))



if __name__=="__main__":
    main()
