import multiprocessing


def factorial(no):
    fact=1
    for i in range(1,no+1):
        fact=fact*i
    return fact
    


def main():
     numbers=input("Enter the five numbers:").split()
     data=[int(num) for num in numbers]
     p=multiprocessing.Pool()
     result=list(map(factorial,data))
     p.close()
     p.join()
     print(result)


if __name__=="__main__":
    main()