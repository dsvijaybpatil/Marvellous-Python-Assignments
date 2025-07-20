import pandas as pd
import numpy as np

def CreateDataFrame():
    data={"Name":["Amit","Sagar","Pooja"],"Math":[np.nan,76,85],
    "Science":[91,np.nan,85],"English":[75,85,82]}
    df=pd.DataFrame(data) 
    mean1=df["Math"].mean()
    df.fillna(mean1,inplace=True)
    mean2=df["Science"].mean()
    df.fillna(mean2,inplace=True)
    print(df)

    




def main():
    CreateDataFrame()
if __name__=="__main__":
    main()