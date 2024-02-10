import pandas as pd

df = pd.read_csv('../data/FinalData.csv')

# print(df.groupby(['Product_Category', 'Product_Sub_Category']).Profit.sum())
# print(df.groupby(['Product_Category', 'Product_Sub_Category'])[['Product', 'Sales']].mean()) #ERROR

### indexing
# iloc [rows, columns] -
# print(df.iloc[4:9, 1:3])

# loc - [rowNames, columnNames]
print(df.loc[1:5, ['Customer_Name', 'Ship_Mode', "Profit"]])
print(df.loc[[25,75,50,100], ['Customer_Name', 'Ship_Mode', "Profit"]])
