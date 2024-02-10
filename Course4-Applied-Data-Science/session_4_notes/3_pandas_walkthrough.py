import pandas as pd
import numpy as np

prod_data = pd.read_csv('../data/prod_dimen.csv')
# print(prod_data.shape)
# print(prod_data.sample(3))

market_data = pd.read_csv('../data/market_fact.csv')
# print(market_data.shape)
# print(market_data.sample(3))
# print(market_data.columns)
# print(market_data.dtypes) # categorical data = "object"
# print(market_data.describe())


### JOINS
# left join
# right join
# inner join - only common records
# outer join - only non-common records
market_prod = pd.merge(prod_data, market_data, on='Prod_id', how='outer')
# print(len(prod_data.columns), len(market_data.columns), len(market_prod.columns))
# print(market_prod)
# print(market_prod.Product_Category.unique())  # list of unique values
# print(market_prod.Product_Category.nunique())  # num of unique values
# print(market_prod.Product_Sub_Category.unique())
# print(market_prod.Product_Sub_Category.nunique())
# print(market_prod.Product_Category.value_counts())
# print(market_prod.Product_Category.value_counts(normalize=True))  # Percentage of occurrence

cus_data = pd.read_csv('../data/cust_dimen.csv')
# print(cus_data.shape)
# print(cus_data.columns)
# print(market_prod.columns)
market_prod_cust = pd.merge(cus_data, market_prod, on='Cust_id', how='outer')
# print(market_prod_cust)

ship_data = pd.read_csv('../data/shipping_dimen.csv')
# print(ship_data.shape)
# print(ship_data.columns)
# print(market_prod_cust.columns)
df = combined_data = pd.merge(market_prod_cust, ship_data, on='Ship_id', how='outer')
# print(combined_data.shape)
# print(combined_data.columns)  # columns are called "features"
combined_data.to_csv('../data/FinalData.csv', index=False)

# print(df.describe().T)  # transpose
# print(df.Customer_Name.nunique())
# print(df.Region.unique())
# print(df.Customer_Segment.value_counts())
# print(df.Customer_Segment.value_counts(normalize=True))
# print(df.Profit.mean())
# print(df.groupby(['Product_Category']).Profit.mean())
# print(df.groupby(['Product_Sub_Category']).Profit.mean())

