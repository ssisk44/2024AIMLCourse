import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset('tips')

sns.boxplot(x='day', y='total_bill', data=df)
plt.show()

sns.violinplot(x='smoker', y='total_bill', data=df)
plt.show()

sns.boxenplot(x='sex', y='tip', data=df)
plt.show()