import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn.ensemble import VotingClassifier
def main():
    data1=pd.read_csv("True.csv")
    
    data2=pd.read_csv("Fake.csv")
    
    data1["Label"]=1
    data2["Label"]=0
    
    Combine_data=pd.concat([data1,data2],ignore_index=True)
    print(Combine_data.head())
    vectorizer=TfidfVectorizer()
    X=vectorizer.fit_transform(Combine_data["title"])
    Y=Combine_data["Label"]
    print(Y.isna().sum())
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
    model1=LogisticRegression()
    model1.fit(x_train,y_train)
    y_pred=model1.predict(x_test)
    Accuracy=accuracy_score(y_test,y_pred)
    print("Accuracy of the Model using Logistic Regression is:",Accuracy*100)
    cm=confusion_matrix(y_test,y_pred)
    print("Confusion matrix of Logistic Regression is:\n",cm)
    disp=ConfusionMatrixDisplay(cm)
    disp.plot(colorbar="green")
    plt.title("Confusion matrix of Logistic Regression")
    plt.show()
    model2=DecisionTreeClassifier()
    model2.fit(x_train,y_train)
    y_pred=model2.predict(x_test)
    Accuracy=accuracy_score(y_test,y_pred)
    print("Accuracy of the Model using Decision Tree Classifier is:",Accuracy*100)
    cm=confusion_matrix(y_test,y_pred)
    print("Confusion matrix of Decision tree Classifier is:\n",cm)
    disp=ConfusionMatrixDisplay(cm)
    disp.plot(colorbar="green")
    plt.title("Confusion matrix of Decision Tree Classifier")
    plt.show()
    voting_clf=VotingClassifier(
        estimators=[("lr",model1),('dt',model2)],
        voting="hard")
    voting_clf.fit(x_train,y_train)
    y_pred2=voting_clf.predict(x_test)
    print("Accuracy of the model by using Ansemble Technique LR VS DTC with Hard voting is:")
    print(accuracy_score(y_test,y_pred2)*100)
    voting_clf2=VotingClassifier(
        estimators=[("lr",model1),('dt',model2)],
        voting="soft")
    voting_clf2.fit(x_train,y_train)
    y_pred3=voting_clf2.predict(x_test)
    print("Accuracy of the model by using Ansemble Technique LR VS DTC with Soft voting is:")
    print(accuracy_score(y_test,y_pred3)*100)

    


if __name__=="__main__":
    main()