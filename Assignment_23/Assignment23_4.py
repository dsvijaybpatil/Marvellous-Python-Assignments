import pandas as pd

def CreateDataFrame():
    data={"Name":["Amit","Sagar","Pooja"],"Math":[85,90,78],
    "Science":[92,88,80],"English":[75,85,82]}
    df=pd.DataFrame(data)
    for index,rows in df.iterrows():
        if rows["Science"]>85:
            print(rows["Name"])




def main():
    CreateDataFrame()
if __name__=="__main__":
    main()