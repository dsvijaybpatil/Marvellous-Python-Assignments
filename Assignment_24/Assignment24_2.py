import pandas as pd

def OneHotEncoding():
    data={"Name":["Amit","Sagar","Pooja"],"Math":[85,90,78],
    "Science":[92,88,80],"English":[75,85,82]}
    df=pd.DataFrame(data)
    df.insert(4,"Gender",["Male","Male","Female"])
    df_Encoded=pd.get_dummies(df,columns=["Gender"])
    

    line="*"*85
    print(line)
    print("Dataframe after One-Hot Encoding is:")
    print(line)
    print(df_Encoded)
    print(line)

    
    






def main():
    OneHotEncoding()
if __name__=="__main__":
    main()