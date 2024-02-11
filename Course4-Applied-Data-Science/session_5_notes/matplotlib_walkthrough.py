import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



### bivariate data
# line chart (time-series/histogram)
# year = [1950, 1970, 1990, 2010]
# pop = [2.3, 3.4, 4.5, 6]
# plt.plot(year, pop)
# plt.xlabel('Year')
# plt.ylabel('Population')
# plt.title("Population over Time")
# plt.show()

# scatterplot
# ht = [140, 155, 176, 160, 180]
# wt = [45, 56, 78, 63, 84]
# plt.scatter(ht, wt)
# plt.xlabel('Height (cm)')
# plt.ylabel('Weight (kg)')
# plt.title("BMI Chart")
# plt.show()

# bar chart
# education_qualifications = ['UG', 'PG', 'PHD']
# frequency = [3,2,2]
# plt.bar(education_qualifications, frequency)
# plt.show()

# frequency chart
# marks = [20,21,14,78,65,34,67,90,54,23,98,54,34,67,32,9]
# plt.hist(marks, bins=5, color='red')
# plt.show()

# pie chart
education_qualifications = ['UG', 'PG', 'PHD']
frequency = [3,2,2]
plt.pie(frequency, labels=education_qualifications)
plt.show()


