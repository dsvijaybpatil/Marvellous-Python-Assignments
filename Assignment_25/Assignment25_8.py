import pandas as pd
import numpy as np

def Interpolation():
    data={"Marks":[85,np.nan,90,np.nan,95]}
    df=pd.DataFrame(data)
    df_Interpol=df.interpolate(method="linear")
    print(df_Interpol)
    
    
    
    

    
    






def main():
    Interpolation()
if __name__=="__main__":
    main()