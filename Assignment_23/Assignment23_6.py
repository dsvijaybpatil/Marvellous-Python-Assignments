import pandas as pd

def CreateDataFrame():
    data={"Name":["Amit","Sagar","Pooja"],"Math":[85,90,78],
    "Science":[92,88,80],"English":[75,85,82]}
    df=pd.DataFrame(data)    
    df.insert(4,"Total",[252,263,240])
    Sorted_df=df.sort_values(by="Total",ascending=False)
    print(Sorted_df)




def main():
    CreateDataFrame()
if __name__=="__main__":
    main()