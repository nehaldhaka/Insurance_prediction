#1. load raw data
#2. indentifying x and y (input and output)
#3. After EDA - Split data into train and test 


#1.
import pandas as pd

data=pd.read_csv("../data/raw/insurance_data.csv")
print(data.head())

#2.
from sklearn.model_selection import train_test_split
 
def load_and_Split_data():
    data=pd.read_csv("../data/raw/insurance_data.csv")
    X=data[['Age','Annual_Income_LPA','Policy_Term_Years','Sum_Assured_Lakhs']]
    y=data['Annual_Premium_Thousands']
    print(X)
    print(y)

#3.
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
    return X_train,X_test,y_train,y_test
 
 