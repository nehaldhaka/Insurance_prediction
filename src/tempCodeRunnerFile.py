def load_and_Split_data():
    data=pd.read_csv("../data/raw/insurance_data.csv")
    X=data[['Age','Annual_Income_LPA','Policy_Term_Years','Sum_Assured_Lakhs']]
    y=data['Annual_Premium_Thousands']
