import pandas as pd
import matplotlib.pyplot as plt

def CreateDataFrame():
    data={"Name":["Amit","Sagar","Pooja"],"Math":[85,90,78],
    "Science":[92,88,80],"English":[75,85,82]}
    df=pd.DataFrame(data)    
    df.insert(4,"Total",[252,263,240])
    X=["Math","Science","English"]
    Y=[85,92,75]
    plt.title('Line Chart of "Amit" marks')
    plt.figure(figsize=(8,5))
    plt.plot(X,Y,color="red")
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    plt.show()

   




def main():
    CreateDataFrame()
if __name__=="__main__":
    main()