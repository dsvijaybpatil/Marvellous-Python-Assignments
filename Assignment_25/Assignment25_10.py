import pandas as pd
from sklearn.model_selection import train_test_split

def DataForML():
    data={"Age":[25,30,45,35,22],"Salary":[50000,60000,80000,65000,45000],
    "Purchased":[1,0,1,0,1]}
    df=pd.DataFrame(data)
    X=df.drop("Purchased",axis=1)
    Y=df["Purchased"]
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
     

    line="*"*85
    print(line)
    print("Data after Splitting is:")
    print(line)
    print("Independent variable training data:\n",X_train)
    print("Dependent variable training data:\n",Y_train)
    print("Independent variable testing data:\n",X_test)
    print("Dependent variable training data:\n",Y_test)   






def main():
    DataForML()
if __name__=="__main__":
    main()