import pandas as pd
import numpy as np

def ReplaceValues():
    data={"Marks":[45,67,88,32,76]}
    df=pd.DataFrame(data)
    df["Marks"]=np.where(df["Marks"]<50,"Fail",df["Marks"])
    line="*"*80
    print(line)
    print("Data after the replacement is:")
    print(line)
    print(df)
    
    
    
    

    
    






def main():
    ReplaceValues()
if __name__=="__main__":
    main()