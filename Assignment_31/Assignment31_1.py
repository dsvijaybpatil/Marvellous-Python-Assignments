import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier,VotingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay,classification_report,roc_auc_score,roc_curve
from sklearn.model_selection import train_test_split

def RandomForest(x_train,x_test,y_train,y_test):
    model=RandomForestClassifier()
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    Accuracy=accuracy_score(y_test,y_pred)
    print("Accuracy of the model using Random Forest classifier is:",Accuracy*100)
    cm=confusion_matrix(y_test,y_pred)
    print("Confusion matrix of the model suing Random forest Classifier is:\n",cm)
    disp=ConfusionMatrixDisplay(cm)
    disp.plot(colorbar="green")
    plt.title("Confusion matrix for Random Forest classifier")
    plt.show()
    cr=classification_report(y_test,y_pred)
    print("Classification report of Random forest classifier is:\n",cr)
    ROC_AUC=roc_auc_score(y_test,y_pred)
    print("ROC-AUC for Random Forest Classifier is:",ROC_AUC)
    fpr,tpr,thresholds=roc_curve(y_test,y_pred)
    plt.figure(figsize=(8,5))
    plt.plot(fpr,tpr)
    plt.xlabel("False Positve Rate")
    plt.ylabel("True positive Rate")
    plt.title("ROC-AUC curve for Random Forest classifier")
    plt.show()
    importance=pd.Series(model.feature_importances_)
    importance=importance.sort_values(ascending=False)                  #Bars will show in descending orders cause of false

    importance.plot(kind="bar",figsize=(10,6),title="Feauture IMP")
    plt.show()
    model2=DecisionTreeClassifier(max_depth=7)
    voting_clf=VotingClassifier(
        estimators=[("rf",model),('dt',model2)],
        voting="hard")
    voting_clf.fit(x_train,y_train)
    y_pred2=voting_clf.predict(x_test)
    print("Accuracy of the model by using Ansemble Technique RF VS DTC is:")
    print(accuracy_score(y_test,y_pred2)*100)

def GradientBoosting(x_train,x_test,y_train,y_test):
    model=GradientBoostingClassifier()
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    Accuracy=accuracy_score(y_test,y_pred)
    print("Accuracy of the model using Gradient Boosting classifier is:",Accuracy*100)
    cm=confusion_matrix(y_test,y_pred)
    print("Confusion matrix of the Gradient Boosting Classifier is;\n",cm)
    disp=ConfusionMatrixDisplay(cm)
    disp.plot(colorbar="red")
    plt.title("Confusion matrix Display fro Gradient Boosting Algorithm.")
    plt.show()
    cr=classification_report(y_test,y_pred)
    print("Classification Report using Gradient Boosting Algorithm.\n",cr)
    ROC_AUC=roc_auc_score(y_test,y_pred)
    print("ROC-AUC for Gradient Boosting Classifier is:",ROC_AUC)
    fpr,tpr,thresholds=roc_curve(y_test,y_pred)
    plt.plot(fpr,tpr)
    plt.title("ROC-AUC curve for Gradient Boosting algorithm")
    plt.xlabel("False positive Rate")
    plt.ylabel("True postive Rate")
    plt.show()
    importance=pd.Series(model.feature_importances_)
    importance=importance.sort_values(ascending=False)
    importance.plot(kind="bar",figsize=(8,6),title="Feature IMP")
    plt.show()
    model2=DecisionTreeClassifier(max_depth=7)
    voting_clf=VotingClassifier(
        estimators=[("gb",model),('dt',model2)],
        voting="hard")
    voting_clf.fit(x_train,y_train)
    y_pred2=voting_clf.predict(x_test)
    print("Accuracy of the model by using Ansemble Technique GB VS DTC is:")
    print(accuracy_score(y_test,y_pred2)*100)




def main():
    cancer=load_breast_cancer()
    X=cancer.data
    Y=cancer.target
    scale=StandardScaler()
    X_scaled=scale.fit_transform(X)
    x_train,x_test,y_train,y_test=train_test_split(X_scaled,Y,test_size=0.2,random_state=42)
    RandomForest(x_train,x_test,y_train,y_test)
    GradientBoosting(x_train,x_test,y_train,y_test)

if __name__=="__main__":
    main()