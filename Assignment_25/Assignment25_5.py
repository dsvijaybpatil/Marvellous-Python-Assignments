import pandas as pd
from sklearn.model_selection import train_test_split
def SplitData():
    data={"Age":[22,25,47,52,46,56],"Purchased":[0,1,1,0,1,0]}
    df=pd.DataFrame(data)
    X=df["Age"]
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
    SplitData()
if __name__=="__main__":
    main()