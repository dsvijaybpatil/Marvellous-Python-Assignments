def TotalEvenNumbers():
    i=1
    count=0
    while(i<=100):
        if i%2==0:
            count+=1
            
        i+=1
    print(count)

if __name__=="__main__":
    TotalEvenNumbers()