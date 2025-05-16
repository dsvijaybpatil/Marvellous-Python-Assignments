def pattern():
    n=int(input("Entr the value:"))
    for i in range(n):
        for j in range(n):                
            print("*",end=" ")             # * will dispay n times for first row then second row then third and so on...
        print()                           # it will shift to the next row


if __name__=="__main__":
    pattern()
