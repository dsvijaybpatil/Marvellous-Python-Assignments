import pandas as pd
import matplotlib.pyplot as plt

def CreateDataFrame():
    data={"Name":["Amit","Sagar","Pooja"],"Math":[85,90,78],
    "Science":[92,88,80],"English":[75,85,82]}
    df=pd.DataFrame(data)    
    df.insert(4,"Total",[252,263,240])
    X=df["Name"]
    Y=df["Total"]
    plt.bar(X,Y,color="red")
    plt.xlabel("Name of the Students")
    plt.ylabel("Total marks of the students")
    plt.title("Bar plot of Name VS Total marks")
    plt.show()




def main():
    CreateDataFrame()
if __name__=="__main__":
    main()