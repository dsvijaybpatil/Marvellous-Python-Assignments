import pandas as pd

def Encoding():
    data={"Grade":["A+","B","A","C","B+"]}
    df=pd.DataFrame(data)
    df["Grade"]=df["Grade"].map({"A+":"Excellent","A":"Very Good","B+":"Good","B":"Average","C":"Poor"})
    line="*"*85
    print(line)
    print("Encoded Data is:\n")
    print(line)
    print(df)
    
    
    

    
    






def main():
    Encoding()
if __name__=="__main__":
    main()