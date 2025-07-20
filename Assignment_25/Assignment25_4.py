import pandas as pd
from sklearn.preprocessing import LabelEncoder
def OneHotEncoding():
    data={"Department":["HR","IT","Finance","HR","IT"]}
    df=pd.DataFrame(data)
    df_Encoded=pd.get_dummies(df,columns=["Department"])
    

    line="*"*85
    print(line)
    print("Dataframe after One-Hot Encoding is:")
    print(line)
    print(df_Encoded)
    print(line)
    

    
    






def main():
    OneHotEncoding()
if __name__=="__main__":
    main()