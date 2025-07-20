import pandas as pd

def CreateDataFrame():
    data={"Name":["Amit","Sagar","Pooja"],"Math":[85,90,78],
    "Science":[92,88,80],"English":[75,85,82]}
    df=pd.DataFrame(data)
    print(df.describe())  # Describe function used to display statistic of the data inside datafrmane like mean,
                          #mean,number of rows,minimum value,maximum valued,std deviation and Quartitles of the data






def main():
    CreateDataFrame()
if __name__=="__main__":
    main()