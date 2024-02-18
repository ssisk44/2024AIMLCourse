import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# df = pd.read_csv('../data/tips.csv', index_col=False)
# df = df[['total_bill', 'tip', 'size']]
# x = df.corr()
# print(x)

df = pd.read_csv('50startups.csv', index_col=False)
# df = df[['R&D Spend', 'Administration', 'Marketing Spend', 'Profit']]
# # x = df.corr()
# # print(x)
# plt.scatter(df['R&D Spend'], df['Profit'])
# plt.show()

##### Hypothesis Testing
from scipy.stats import pearsonr
# """
# Null hypothesis typically defines no relationship
# ho : R&D Spend and Profit has no correlation
# ha : R&D Spend and Profit has correlation
#
# significance level : alpha = 0.05
# """
# alpha = 0.05
# corr, p_val = pearsonr(df['R&D Spend'], df['Profit'])
# print("Correlation: ", corr)
# print("p-value: ", p_val)
# """
# Correlation:  0.9729004656594831
# p-value:  3.5003222436905986e-32
# p-value < 0.05 => reject ho
# """
# if p_val < alpha:
#     print('Reject ho => Accept ha')
# else:
#     print('Accept ho')


# """
# ho : R&D Spend and Profit has no correlation
# ha : R&D Spend and Profit has correlation
#
# significance level : alpha = 0.05
# """
# alpha = 0.05
# corr, p_val = pearsonr(df['Marketing Spend'], df['Administration'])
# print("Correlation: ", corr)
# print("p-value: ", p_val)
# """
# Correlation:  0.9729004656594831
# p-value:  3.5003222436905986e-32
# p-value < 0.05 => reject ho
# """
# if p_val < alpha:
#     print('Reject ho => Accept ha')
# else:
#     print('Accept ho')


# from scipy.stats import normaltest
# #### NORMAL DISTRIBUTION
# """
# ho : Normal distribution
# ha : Not normal distribution
# """
# alpha = 0.05
# stat,p_val = normaltest(df['R&D Spend'])
# print("p-value: ", p_val)
# if p_val < alpha:
#     print('Reject ho => Accept ha')
# else:
#     print('Accept ho')


# from scipy.stats import shapiro
# """
# ho : Normal distribution
# ha : Not normal distribution
# """
# alpha = 0.05
# stat,p_val = shapiro(df['R&D Spend'])
# print("p-value: ", p_val)
# if p_val < alpha:
#     print('Reject ho => Accept ha')
# else:
#     print('Accept ho')


# from scipy.stats import shapiro
# """
# ho : Normal distribution
# ha : Not normal distribution
# """
# alpha = 0.05
# stat,p_val = shapiro(df['Administration'])
# print("p-value: ", p_val)
# if p_val < alpha:
#     print('Reject ho => Accept ha')
# else:
#     print('Accept ho')


### T-TEST
from scipy import stats
# ht_g = stats.norm.rvs(# print("p-value: ", p_val)
# ht_f = stats.norm.rvs(loc=168, scale=9, size=25, random_state=100)
# print("Average German height:",ht_g.mean())
# print("Average French height:",ht_f.mean())
# """
# ho: No difference in mean of 2 groups
# ha: there is a difference in mean of 2 groups
#
# alpha = 0.05
# """
# alpha = 0.05
# stat,p_val = stats.ttest_ind(ht_g, ht_f)
# print("p-value: ", p_val)
# if p_val < alpha:
#     print('Reject ho => Accept ha')
# else:
#     print('Accept ho')

# """
# ho: mean is same
# ha: mean is different
# alpha = 0.05
# """
# pizza_size = stats.norm.rvs(loc=29, scale=2, size=20, random_state=100)
# pizza_standard_size = 30
# # print("average pizza size: ", pizza_size.mean())
# stats, p_val = stats.ttest_1samp(pizza_size, pizza_standard_size)
# print("p-value: ", p_val)
# alpha = 0.05
# if p_val < alpha:
#     print('Reject ho => Accept ha => mean size of pizza is different from claim')
# else:
#     print('Accept ho => mean pizza size is what was claimed')

# df = pd.read_csv('bp.csv')
# # print(df.shape, df.head())
# print(df['bp_before'].mean())
# print(df['bp_after'].mean())
# """
# ho: no difference in bp from treatment => treatment not effective
# ha: difference in bp from treatment => treatment is effective
# alpha = 0.05
# """
# stats,p_val = stats.ttest_rel(df['bp_before'], df['bp_after'])
# print("p-value: ", p_val)
# alpha = 0.05
# if p_val < alpha:
#     print('Reject ho => Accept ha => treatment not effective')
# else:
#     print('Accept ho => treatment is effective')


#### CHI SQUARED TEST
# df = sns.load_dataset('tips')
# # print(df.head())
# table = pd.crosstab(df.sex, df.smoker, normalize='index')*100
# # print(table)
# """
# Is smoking a gender dependent behavior?
# ho: behaviour is independent
# ha: behaviour is dependant
# """
# stats, p_val, dof, expected = stats.chi2_contingency(table)
# alpha = 0.05
# print("p-value: ", p_val)
# if p_val < alpha:
#     print('Reject ho => Accept ha => behaviour is independent')
# else:
#     print('Accept ho => behaviour is dependant')

#### ANOVA
import numpy as np
from scipy.stats import f_oneway
"""
Is there a difference in the mean of the groups? (if only one group differs then ha)
ho: there is no difference in the mean of the groups
ha: there is a difference in the mean of the groups
"""
traditional_lectures = np.array([80, 85, 75, 90, 95])
online_lectures = np.array([75, 70, 85, 80, 90])
interactive_workshop = np.array([85, 82, 88, 80, 90])
stats,p_val = f_oneway(traditional_lectures, online_lectures, interactive_workshop)
alpha = 0.05
print("p-value: ", p_val)
if p_val < alpha:
    print('Reject ho => Accept ha => difference')
else:
    print('Accept ho => no difference')


