import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
# print(df.shape)
#
# print(df.info())
# print(df.describe())
# average tip
# print('total bill: ', df.groupby(['sex', 'smoker', 'size']).total_bill.mean())
# print('avg tip: ', df.groupby(['sex', 'smoker', 'size']).tip.mean())
# print('total bill: ', df.groupby(['size']).total_bill.mean())
# print('avg tip: ', df.groupby(['size']).tip.mean())
# print('total bill: ', df.groupby(['size']).total_bill.mean())
# print('avg tip: ', df.groupby(['size']).tip.mean())
# tip by gender

# plt.hist(df['total_bill'])
# plt.show()

# print(df.sex.value_counts())
# print(df.sex.value_counts(normalize=True))
# print(df.smoker.value_counts(normalize=True))
# print(df.day.value_counts(normalize=True))
# print(df.time.value_counts(normalize=True))

# print(df.dtypes)
# categorical = df.select_dtypes(['category']).columns
# df[categorical] = df[categorical].apply(lambda x: pd.factorize(x)[0])
# sns.pairplot(df, hue="smoker")
# plt.show()

# print(df.time.unique())
# df.time.value_counts().plot(kind='bar',)
# plt.show()

### seaborn method is much simpler than matplotlib for charting
# sns.countplot(x='day', data=df)
# plt.show()
# sns.countplot(x='smoker', data=df)
# plt.show()
# sns.countplot(x='time', data=df)
# plt.show()

# day_ft = df.day.value_counts()
# plt.pie(day_ft, labels=df.day.unique(), autopct='%1.1f%%')
# plt.show()

# sns.barplot(x='day', y='total_bill', data=df)
# plt.show()

# sns.regplot(x='total_bill', y='tip', data=df)
# plt.show()
# plt.scatter(df.total_bill, df.tip)
# plt.show()

### Strip plot
# sns.stripplot(x='total_bill', y='tip', data=df, jitter=True)
# plt.show()
#
# sns.stripplot(x='day', y='total_bill', data=df, jitter=True)
# plt.show()