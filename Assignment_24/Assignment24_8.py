import pandas as pd
import matplotlib.pyplot as plt

def CreateDataFrame():
    data={"Name":["Amit","Sagar","Pooja"],"Math":[85,90,78],
    "Science":[92,88,80],"English":[75,85,82]}
    df=pd.DataFrame(data)  
    df.insert(4,"Gender",["Male","Male","Female"])
    df.insert(5,"Total",[252,263,240])  
    
    plt.figure(figsize=(8,5))
    
    plt.hist(df["Math"])
    plt.title("Histogram of Math Marks")
    
    plt.show()
   




def main():
    CreateDataFrame()
if __name__=="__main__":
    main()