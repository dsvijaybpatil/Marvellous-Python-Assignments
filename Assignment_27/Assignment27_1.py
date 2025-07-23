import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def AdvertisingLinearRegression(Datapath):
       data=pd.read_csv(Datapath)
       df=pd.DataFrame(data)
       print(df.head())
       print(df.shape)
       df.drop(columns=["Unnamed: 0"],axis=1,inplace=True)
       X=df.drop(columns=["sales"],axis=1)
       Y=df["sales"]
       print(X.shape)
       print(Y.shape)
       X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.5,random_state=42)
       model=LinearRegression()
       model.fit(X_train,Y_train)
       Y_pred=model.predict(X_test)
       line="*"*80
       print(line)
       print("Predicted Value of the Dataset by using Linear Regression Model is:")
       print(line)
       print(Y_pred)
       print(line)
       print("Actual Value of the Dataset is:")
       print(line)
       print(Y_test)

       
                      
                             

      
def main():
        AdvertisingLinearRegression("MarvellousAdvertising.csv")        
        
        
        

if __name__=="__main__":
     main()

