import pandas as pd
import numpy as np

### Dataframe from dictionary
dict1 = {
    'SrNo': [1, 2, 3, 4],
    'Name': ['Benjamin', 'Udaram', 'Austin', 'Samuel'],
    'Number': [3, 4, 5, 6]
}
# print(dict1)
df = pd.DataFrame(dict1)
# # print(type(df))
# # print(df)
# # print(df.shape)
# # print(df.columns)
# df["City"] = ["Denver", "Topeka", "Raleigh", "New York City"]
# df["Country"] = ["Norway", "Spain", "India", 'USA']
# df["Test"] = 'test'
# df = df.drop(["City", "Country", "Test"], axis=1)  # axis 1 = column
### inplace=True is the same as df = df.drop... reassignment
# df.drop(2, axis=0, inplace=True)  # axis 0 = row




### Dataframe from CSV
# df = pd.read_csv('binary.csv')
# print(df.shape)
# print(df.dtypes)
# print(df.head(10))
# print(df.tail(2))
# df.sample(4)
# print(df.describe())
# print(df.info())
# print(df.gre)
# print(df[df.gre > 795].shape) #filtering
# print(df[(df.gpa > 3) & (df.gre < 350)])
# print(df[(df.gpa<2.7) | (df.gre > 795)])
# print(df[['gre', 'gpa']])
# df3 = df.sample(7)
# df3.sort_values(by='gpa', ascending=False, inplace=True)
# print(df3)

### concatenation
# df10 = pd.DataFrame(np.arange(9).reshape(3,3), columns=['SrNo', 'Name', 'Number'])
# df11 = pd.DataFrame(np.arange(12).reshape(4,3), index=["R1", "R2", "R3", "R4"], columns=['SrNo', 'Name', 'Number'])
# print(df10, "\n", df11)
# df_res1 = pd.concat([df10, df11], axis=0)
# print(df_res1)

df20 = pd.DataFrame(np.arange(12).reshape(4,3), columns=['Grade','DoB','Address'])
df_res2 = pd.concat([df, df20], axis=1)  # axis: 1 = columns, 0 = rows
print(df_res2)
print(df_res2.Number.mean())