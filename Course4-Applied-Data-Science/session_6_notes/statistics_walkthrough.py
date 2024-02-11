import pandas as pd
import seaborn as sns
import numpy as np

df = sns.load_dataset('tips')
"""
inner quartile range (IQR) = Q3 - Q1
upper cuttoff = Q3 + 1.5 x IQR => outlier > upper cutoff
lower cutoff = Q1 - 1.5 x IQR => outlier < lower cutoff

"""

"""
print(df.total_bill.describe())
count    244.000000
mean      19.785943
std        8.902412
min        3.070000
25%       13.347500
50%       17.795000
75%       24.127500
max       50.810000
"""
# Q3 = df.total_bill.quantile(0.75)
# Q1 = df.total_bill.quantile(0.25)
# IQR = Q3 - Q1
# UC = round(Q3 + 1.5 * IQR, 2)
# LC = round(Q1 - 1.5 * IQR, 2)
# outliers = df[(df.total_bill > UC) | (df.total_bill < LC)]
# print(outliers)

# q3 = df.tip.quantile(0.75)
# q1 = df.tip.quantile(0.25)
# iqr = q3 - q1
# uc = round(q3 + 1.5 * iqr, 2)
# lc = round(q1 - 1.5 * iqr, 2)
# outliers = df[(df.tip > uc) | (df.tip < lc)]
# print(iqr, uc, lc)
# print(outliers)

"""
EDA (Exploratory Data Analysis)
- missing values (null or missing) - NaN
- outliers
- data transformation

"""

### MISSING VALUES
# print(df.shape)
# print(df.head())
# print(df.info())
# print(df.isnull().sum())  # missing values count
"""
replace missing CATEGORICAL values with MODE
replace missing NUMERICAL values with 
    - MEAN
    - MEDIAN - when data has outliers (mean is outlier sensitive)

or 

if there are a large amount of nul values (30-40-50%) then you can drop the column
"""

### NORMAL DISTRIBUTION
"""
pdf = normal distribution curve (NDC)
1) bell shaped curve 
2) mean ~= median ~= mode
3) symmetric around mean

- left/right skewed contain outliers on the opposite side of the skewed mean
"""

# df = pd.DataFrame([
#     [np.nan, 2, np.nan, 0, 4],
#     [3, 4, np.nan, np.nan, 2],
#     [np.nan, np.nan, np.nan, 5, 3],
#     [np.nan, 3, np.nan, 4, 2],
#     [0, 1, 2, np.nan, np.nan],
# ], columns=list('ABCDE'))
# print(df.isnull().sum())
# print(df.mean())
# print(df.median())
# df = df.fillna(df.mean())  # filling empty values with each columns mean
# print(df)

# df['E'] = df.E.fillna(df.E.median())  # filling E column with E column mean

"""
filling values - replaces next value in a column, if is NaN, with previous value
    1) fill forward - top down per column
    2) fill backward - bottom up per column
    * if NaN/s appear before the first value they are not changed
    * good for time series data
"""
# df_ffill = df.fillna(method='ffill')
# df_bfill = df.fillna(method='bfill')
# print(df_ffill, '\n', df_bfill)

"""
Filling categorical variables
"""
# df = pd.DataFrame([
#     [np.nan, 2, np.nan, 0, 'Male'],
#     [3, 4, np.nan, np.nan, 'Female'],
#     [np.nan, np.nan, np.nan, 5, 'Male'],
#     [np.nan, 3, np.nan, 4, 'Male'],
#     [0, 1, 2, np.nan, np.nan],
# ], columns=list('ABCDE'))

# print(df.E.mode())
# print(df.E.value_counts())
### male appears more frequently so we replace missing values accordingly
# df_cat = df.fillna({'E': "Male"})
# print(df_cat)

df = pd.read_csv('../data/missing_values.csv')
print(df.shape)
print(df.isnull().sum())
"""
HOMEWORK ASSIGNMENT
- Analyze loan data and come up with insights
"""
