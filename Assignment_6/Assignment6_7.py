def Largest(value):
    max=value[0]
    for i in range(1,len(value)):
        if max<=value[i]:
            max=value[i]
       
    print("Maximum Number is:",max)
    


def main():
     numbers=input("Enter the five numbers:").split()
     data=[int(num) for num in numbers]
     Largest(data)  



if __name__=="__main__":
    main()