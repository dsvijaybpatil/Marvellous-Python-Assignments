import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
def WinePredictorClassification(X_train,X_test,Y_train,Y_test):
             
       model=DecisionTreeClassifier()
       model.fit(X_train,Y_train)
       Y_pred=model.predict(X_test)
       Accuracy=accuracy_score(Y_test,Y_pred)
       print("Accuracy for the given data using Decision tree Classifier is:",Accuracy*100)

def WinePredictorKKN(X_train,X_test,Y_train,Y_test):
       model=KNeighborsClassifier()
       model.fit(X_train,Y_train)
       Y_pred=model.predict(X_test)
       Accuracy=accuracy_score(Y_test,Y_pred)
       print("Accuracy for the given data using model KNN Classifier:",Accuracy*100)

def WinePredictorRandomForest(X_train,X_test,Y_train,Y_test):
       model=RandomForestClassifier()
       model.fit(X_train,Y_train)
       Y_pred=model.predict(X_test)
       Accuracy=accuracy_score(Y_test,Y_pred)
       print("Accuracy for the given data using model Random Forest Classifier:",Accuracy*100)      

                             

      
def main():
        data=pd.read_csv("WinePredictor.csv")
        df=pd.DataFrame(data)
        print(df.head())
        print(df.shape)
        print(df.isnull().sum())
        X=df.drop(columns=["Class"],axis=1)
        Y=df["Class"]
        X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
        WinePredictorClassification(X_train,X_test,Y_train,Y_test)
        WinePredictorKKN(X_train,X_test,Y_train,Y_test)   
        WinePredictorRandomForest(X_train,X_test,Y_train,Y_test)       

        
        
        

if __name__=="__main__":
     main()

