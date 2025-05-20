def Palindrome(s):
    if s==s[::-1]:
        return True
    return False



def main():
    str=input("Enter the String:")
    ans=Palindrome(str)
    if ans:
        print("{} is a palindrome".format(str))
    else:
        print("{} is not a palindrome".format(str))

    
    
    

if __name__=="__main__":
    main()

