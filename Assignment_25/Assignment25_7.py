import pandas as pd

def Normalization():
    data={"Age":[18,22,25,30,34]}
    df=pd.DataFrame(data)
    min_value=df["Age"].min()
    max_value=df["Age"].max()
    df_norm=(df["Age"]-min_value)/(max_value-min_value)
    print("*"*80)
    print("Data after Normalization is:")
    print("*"*80)
    print(df_norm)
    
    
    

    
    






def main():
    Normalization()
if __name__=="__main__":
    main()