x=int(input("Enter First Number:"))
y=int(input("Enter Second Number:"))
z=int(input("Enter Third Number:"))

if x>=y and x>=z:
    print("Largest Number is",x)
elif y>=x and y>=z:
    print("Largest Number is",y)

else:
        print("Largest Number is",z)

    