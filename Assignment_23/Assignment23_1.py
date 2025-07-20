import pandas as pd

def CreateDataFrame():
    data={"Name":["Amit","Sagar","Pooja"],"Math":[85,90,78],
    "Science":[92,88,80],"English":[75,85,82]}
    df=pd.DataFrame(data)
    print(df.columns)    # Columns attributes used to print columns Names of the DataFrame
    print(df.shape)      # shape  attributes used to print dimentaion of the Dataframe
    print(type(df))      # type function is used to print type of the given data type
    print(type(data))






def main():
    CreateDataFrame()
if __name__=="__main__":
    main()