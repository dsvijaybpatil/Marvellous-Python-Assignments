import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay,precision_score,recall_score,f1_score



def DataVisualization(X,Y):
    data=pd.DataFrame(X,Y)
    plt.figure(figsize=(9,5))
    sns.heatmap(data,annot=True,cmap="YlGnBu")
    plt.title("Heat map for Breast_Cancer Data Set")
    plt.xlabel("Features of Data set")
    plt.ylabel("Label for Data set")
    plt.show()

    plt.boxplot(data)
    plt.title('Box plot for Breast_cancer Data set')
    plt.xlabel("Features")
    plt.ylabel("Labels")
    plt.show()
    line="*"*80
    print(line)
    print('Data Summary Statistic of Breast_Cancer Data set:')
    print(line)
    print(data.describe())               # Data Summary statistics using describe method

def LGRegression(X,Y):
    scaler=StandardScaler()
    X_scaled=scaler.fit_transform(X)
    x_train,x_test,y_train,y_test=train_test_split(X_scaled,Y,test_size=0.2,random_state=42)
    model=LogisticRegression()
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    Accuracy=accuracy_score(y_test,y_pred)
    print("Accuracy of the Logistic Regression Model is:",Accuracy*100)
    cm=confusion_matrix(y_test,y_pred)
    print("Confusion Matrix using Logistic Regression:\n",cm)
    disp=ConfusionMatrixDisplay(cm)
    disp.plot(cmap=plt.cm.Blues)
    plt.title('Confusion Matrix for Logistic Regression classsifier')
    plt.show()
    print("Precision Score is:",precision_score(y_test,y_pred))
    print("Recall Score is:",recall_score(y_test,y_pred))
    print("F1 Score is:",f1_score(y_test,y_pred))
    



def BCWDataset():
    cancer=load_breast_cancer()
    X=cancer.data
    Y=cancer.target
    print(np.any(np.isnan(X)))    # to check null values in the given array X
    
    print(np.any(np.isnan(Y)))    # to chech null values in the given array Y
    DataVisualization(X,Y)
    LGRegression(X,Y)


    


def main():
    BCWDataset()
if __name__=="__main__":
    main()