import pandas as pd 
from seaborn import boxplot,pairplot,countplot,heatmap
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,precision_recall_fscore_support,classification_report
from sklearn.linear_model import LogisticRegression


def MarvellousDiabetesVisual(Datapath):
    data=pd.read_csv(Datapath)
    df=pd.DataFrame(data)
    print(df.head())
    print(df.shape)
    print(df.isna().sum())
    print(df.describe())   
    pairplot(df,hue="Age")
    plt.title("Pair plot of Diabetes Data")
    plt.show()

    plt.figure(figsize=(8,5))
    plt.hist(df["Outcome"],bins=10,color="Skyblue",edgecolor='black')
    plt.xlabel("Diabetes Outcome")
    plt.ylabel("Frequency")
    plt.title("Marvellous Histogram of Diabetes Data.")
    plt.show()
    plt.figure(figsize=(8,5))
    countplot(df,x="Outcome",hue="Age").set_title("Countplot for Diabetes vs age")
    plt.show()
    plt.figure(figsize=(8,6))
    boxplot(data=df,x="Outcome",y="BloodPressure")
    plt.title("Maarvellous Box plot of Diabetes Data")
    plt.show()
    X=df.drop(columns=["Outcome"])
    Y=df["Outcome"]
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
    DiabetesDTC(X_train,X_test,Y_train,Y_test)
    DiabetesKNN(X_train,X_test,Y_train,Y_test)
    DiabetesLR(X_train,X_test,Y_train,Y_test)
    


def DiabetesDTC(X_train,X_test,Y_train,Y_test):
    model=DecisionTreeClassifier()
    model.fit(X_train,Y_train)
    Y_pred=model.predict(X_test)
    PData=pd.DataFrame(Y_pred)
    PData.to_csv("DTCPredictedData.csv")              # Store predicted data in into CSV file
    Accuracy=accuracy_score(Y_test,Y_pred)
    print("Accuracy of the model using Decision Classifier is:",Accuracy*100)
    cm=confusion_matrix(Y_test,Y_pred)
    print("Confusion matrix is:\n",cm)
    PRF1Score=precision_recall_fscore_support(Y_test,Y_pred)
    print("Precision Recall and F1 Score is:\n",PRF1Score)
    plt.figure(figsize=(8,5))
    heatmap(cm,annot=True,cmap="Greens")             # Heat map for the Confusion matirix
    plt.title("Heatmap for the confusion Matrix using DTC")
    plt.show()
    

def DiabetesKNN(X_train,X_test,Y_train,Y_test):
    model=KNeighborsClassifier(n_neighbors=7)
    model.fit(X_train,Y_train)
    Y_pred=model.predict(X_test) 
    PData=pd.DataFrame(Y_pred)
    PData.to_csv("KNNPredictedData.csv")
    Accuracy=accuracy_score(Y_test,Y_pred)
    print("Accuracy of the model using KNN Classifier is:",Accuracy*100)
    cm=confusion_matrix(Y_test,Y_pred)
    print("Confusion matrix is:\n",cm)
    plt.figure(figsize=(9,6))
    heatmap(cm,annot=True,cmap="Blues")
    plt.title("Heatmap for confision matrix using KNN")
    plt.show()
    PRF1Score=precision_recall_fscore_support(Y_test,Y_pred)
    print("Precision Recall and F1 Score is:\n",PRF1Score)  
def DiabetesLR(X_train,X_test,Y_train,Y_test):
    model=LogisticRegression()
    model.fit(X_train,Y_train)
    Y_pred=model.predict(X_test) 
    PData=pd.DataFrame(Y_pred)
    PData.to_csv("LRPredictedData.csv")
    Accuracy=accuracy_score(Y_test,Y_pred)
    print("Accuracy of the model using Logistic Regression Classifier is:",Accuracy*100)
    cr=classification_report(Y_test,Y_pred)
    print("Classification Report is:\n",cr)
    PRF1Score=precision_recall_fscore_support(Y_test,Y_pred)
    print("Precision Recall and F1 Score is:\n",PRF1Score)


def main():
    MarvellousDiabetesVisual("MarvellousDiabetes.csv")

if __name__=="__main__":
    main()