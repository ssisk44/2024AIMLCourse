import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# df = pd.read_csv('data/FinalData.csv')
## bivariate
# scatterplot
# line chart (time-series/histogram)
year = [1950, 1970, 1990, 2010]
pop = [2.3, 3.4, 4.5, 6]
plt.plot(year, pop)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title("Population over Time")
plt.show()