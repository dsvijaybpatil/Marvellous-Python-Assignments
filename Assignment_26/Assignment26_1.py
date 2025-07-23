import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
def KNNPlayPredictor(Datapath):
    df=pd.read_csv(Datapath)
    
    print(df.head())
    print(df.shape)
    print(df.isna().sum())
    df.drop(columns=["Unnamed: 0"],inplace=True)
    print(df.head())
    Label=LabelEncoder()
    df["Whether"]=Label.fit_transform(df["Whether"])
    df["Temperature"]=Label.fit_transform(df["Temperature"])
    df["Play"]=df["Play"].map({"No":0,"Yes":1})
    X=df.drop(columns=["Play"],axis=1)
    Y=df["Play"]
        
    model=KNeighborsClassifier(n_neighbors=3)
    model.fit(X,Y)
    
    data={"Whether":[2],"Temperature":[1]}
    X_test=pd.DataFrame(data)
    Y_pred=model.predict(X_test)
    if Y_pred==0:
        print("Predicted Result is: No")
    else:
        print("Predicted Result is: Yes")
    CheckAccuracy(X,Y)
def CheckAccuracy(X,Y):
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.5,random_state=42)
    for k in range(1,16):
        model=KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train,Y_train)
        Y_pred=model.predict(X_test)
        Accuracy=accuracy_score(Y_test,Y_pred)
        print(f"Accuracy of the model for k={k} is:",Accuracy) 



def main():
    KNNPlayPredictor("MarvellousInfosystems_PlayPredictor.csv")
if __name__=="__main__":
    main()