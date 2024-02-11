import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset('tips')

# sns.boxplot(x='day', y='total_bill', data=df)
# plt.show()
#
# sns.violinplot(x='smoker', y='total_bill', data=df, hue='smoker')
# plt.show()
# print(df.groupby(['smoker'])['total_bill'].mean())
#
#
# sns.boxenplot(x='sex', y='tip', data=df)
# plt.show()

"""probability density function"""
# sns.displot(df.total_bill)
# plt.show()

"""for comparison between categorical data"""
print(round(pd.crosstab(df.sex, df.day, normalize='index')*100, 1))  # row

print(round(pd.crosstab(df.sex, df.day, normalize='columns')*100, 1))  # column