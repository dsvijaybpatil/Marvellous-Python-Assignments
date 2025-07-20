import pandas as pd

def CreateDataFrame():
    data={"Name":["A","B","C"],"Age":[21.0,22.0,23.0]}
    df=pd.DataFrame(data)
    line="*"*85
    print(line)
    print("Data types of the Each column in thd Dataframe is:")
    print(df.dtypes)
    print(line)
    df["Age"]=df["Age"].astype(int)
    
    print("Data type of Age Conveted into integer datatype:")
    print(line)
    print(df)

    
    






def main():
    CreateDataFrame()
if __name__=="__main__":
    main()