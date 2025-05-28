import multiprocessing

def Square(values):
    for i in values:
        ans=i**2
        print(ans,end=" ")

        



def main():
    print("Inside the main.")
    data=[65000000,85000000,45000000,95000000,75000000,68888777,8888555555]
    M1=multiprocessing.Process(target=Square,args=(data,))
    M1.start()
    M1.join()
    print()
    print("End of the Programe.")
    

if __name__=="__main__":
    main()

