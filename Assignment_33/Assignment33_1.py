import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def Clustering():
    df=pd.read_csv("student-mat.csv")
    
    X=df.iloc[:,[13,14,29,30,31,32]].values
    print(X.shape)
    print(X)
    model=KMeans(n_clusters=3,init="k-means++",n_init=10,random_state=42)
    y_kmeans=model.fit_predict(X)                   
    print("Values of y_kmeans",y_kmeans)
    

    plt.scatter(X[y_kmeans==0,0],X[y_kmeans==0,1],s=100,c="red",label="G1 Clustor")

    plt.scatter(X[y_kmeans==1,0],X[y_kmeans==1,1],s=100,c="blue",label="G2 Clustor")

    plt.scatter(X[y_kmeans==2,0],X[y_kmeans==2,1],s=100,c="green",label="G3 Clustor")

    plt.scatter(model.cluster_centers_[:,0],model.cluster_centers_[:,1],s=100,c="yellow",label="Centroid")
    plt.legend()
    plt.show()

def main():
    Clustering()




if __name__=="__main__":
    main()