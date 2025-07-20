import pandas as pd

def CreateDataFrame():
    data={"Salary":[25000,27000,29000,31000,50000,100000]}
    df=pd.DataFrame(data)
    Q1=df["Salary"].quantile(0.25)
    Q3=df["Salary"].quantile(0.75)
    IQR=Q3-Q1
    print("IQR of the given data is:",IQR)
    Lower_Bound=Q1-1.5*IQR
    Upper_Bound=Q3+1.5*IQR
    Outliers=df[(df["Salary"]<Lower_Bound) | (df["Salary"]>Upper_Bound )]
    print("The Outliers of the given data is:\n",Outliers)

    
    






def main():
    CreateDataFrame()
if __name__=="__main__":
    main()