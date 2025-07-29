import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix,roc_auc_score,roc_curve,ConfusionMatrixDisplay

def KNN(x_train,x_test,y_train,y_test):
    model=KNeighborsClassifier()
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    Accuracy=accuracy_score(y_test,y_pred)
    print("Accuracy of the model uisng KNN is:",Accuracy*100)
    cm=confusion_matrix(y_test,y_pred)
    print("Confusion matrix using KNN is:\n",cm)
    disp=ConfusionMatrixDisplay(cm)
    
    disp.plot()
    plt.title("Confusion Matrix for KNN")
    cr=classification_report(y_test,y_pred)
    print("Classification report for the model using KNN is:\n",cr)
    roc_auc=roc_auc_score(y_test,y_pred)
    print("ROC and AUC for the model using KNN is:",roc_auc)
    roc_curve(y_test,y_pred)
    fpr, tpr, thresholds = roc_curve(y_test, y_pred)
    plt.figure(figsize=(9,5))
    plt.plot(fpr,tpr)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC curve using KNN")
    plt.show()
def LRegression(x_train,x_test,y_train,y_test):
    model=LogisticRegression()
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    Accuracy=accuracy_score(y_test,y_pred)
    print("Accuracy of the model uisng LR is:",Accuracy*100)
    cm=confusion_matrix(y_test,y_pred)
    print("Confusion matrix using LR is:\n",cm)
    disp=ConfusionMatrixDisplay(cm)
    
    disp.plot()
    plt.title("Confusion Matrix for LR")
    cr=classification_report(y_test,y_pred)
    print("Classification report for the model using LR is:\n",cr)
    roc_auc=roc_auc_score(y_test,y_pred)
    print("ROC and AUC for the model using LR is:",roc_auc)
    roc_curve(y_test,y_pred)
    fpr, tpr, thresholds = roc_curve(y_test, y_pred)
    plt.figure(figsize=(9,5))
    plt.plot(fpr,tpr)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC curve using Logistic Regression ")
    plt.show()

def RandomForest(x_train,x_test,y_train,y_test):
    model=RandomForestClassifier()
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    Accuracy=accuracy_score(y_test,y_pred)
    print("Accuracy of the model uisng Random Forest Classifier is:",Accuracy*100)
    cm=confusion_matrix(y_test,y_pred)
    print("Confusion matrix using Random Forest Classifier is:\n",cm)
    disp=ConfusionMatrixDisplay(cm)
    
    disp.plot()
    plt.title("Confusion Matrix for Random Forest Classifier")
    cr=classification_report(y_test,y_pred)
    print("Classification report for the model using Random Forest Classifier is:\n",cr)
    roc_auc=roc_auc_score(y_test,y_pred)
    print("ROC and AUC for the model using Random Forest Classifier is:",roc_auc)
    roc_curve(y_test,y_pred)
    fpr, tpr, thresholds = roc_curve(y_test, y_pred)
    plt.figure(figsize=(9,5))
    plt.plot(fpr,tpr)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC curve using Random Forest Classifier")
    plt.show()

def main():
    data=pd.read_csv("bank-full.csv")
    data.drop(columns=["job","education","default","contact","month","poutcome"],axis=1,inplace=True)
    model=LabelEncoder()
    data["marital"]=model.fit_transform(data["marital"])
    data["housing"]=model.fit_transform(data["housing"])
    data["loan"]=model.fit_transform(data["loan"])
    data["y"]=model.fit_transform(data["y"])
    line="*"*80
    print(data.head())
    X=data.drop("y",axis=1)
    Y=data["y"]
    print(X.shape,Y.shape)
    
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
    print(line)
    print("Model building by using K-Nearest Algorith.")
    print(line)
    KNN(x_train,x_test,y_train,y_test)
    print(line)
    print("Model building by using Logistic Regression Algorith.")
    print(line)
    LRegression(x_train,x_test,y_train,y_test)
    print(line)
    print("Model building by using Random Forest Classifier Algorith.")
    print(line)
    RandomForest(x_train,x_test,y_train,y_test)

if __name__=="__main__":
    main()
