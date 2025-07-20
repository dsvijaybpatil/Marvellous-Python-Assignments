import pandas as pd

def CreateDataFrame():
    data={"Name":["Amit","Sagar","Pooja"],"Math":[85,90,78],
    "Science":[92,88,80],"English":[75,85,82]}
    df=pd.DataFrame(data)
    min_value=df["Math"].min()
    max_value=df["Math"].max()
    df_norm=(df["Math"]-min_value)/(max_value-min_value)
    print("DataFrame after Normalization is:")
    print(df_norm)

    
    






def main():
    CreateDataFrame()
if __name__=="__main__":
    main()