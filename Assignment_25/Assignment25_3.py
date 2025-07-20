import pandas as pd
from sklearn.preprocessing import LabelEncoder
def LabelEncoding():
    data={"City":["Pune","Mumbai","Delhi","Pune","Delhi"]}
    df=pd.DataFrame(data)
    Label=LabelEncoder()
    df["City"]=Label.fit_transform(df["City"])
    

    line="*"*85
    print(line)
    print("Dataframe after Label Encoding is:")
    print(line)
    print(df)
    print(line)
    

    
    






def main():
    LabelEncoding()
if __name__=="__main__":
    main()