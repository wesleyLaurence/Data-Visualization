""" 
Global Temperature Anomalies
Data Source: https://data.giss.nasa.gov/gistemp/
Chart created by Wesley Laurence
"""

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set_style("whitegrid")

# load datasets
df1 = pd.read_csv('ExcelFormattedGISTEMPDataCSV.csv')
df2 = pd.read_csv('ExcelFormattedGISTEMPData2CSV.csv')

# drop missing values
df1.replace("***", np.nan, inplace=True)
df1.replace("****", np.nan, inplace=True)
df1.dropna(axis=0, inplace=True)

df2.replace("***", np.nan, inplace=True)
df2.replace("****", np.nan, inplace=True)
df2.dropna(axis=0, inplace=True)

# convert values to int type
df1 = df1.astype(int)
df2 = df2.astype(int)

sns.set_style("white")
plt.tight_layout()

# color palette
colors = ['lime' if (x < 0) else 'orangered' for x in df2['SHem'] ]

# create figure and axis
fig, ax = plt.subplots(2, figsize=(12,6))

# Plot 1 settings
ax[0].plot(df2['Year'], df2['SHem'])
ax[0].set_title('Global Annual Temperature Anomalies')
ax[0].tick_params(bottom=True)
ax[0].grid(axis="both")
ax[0].text(40, -215, r"DATA SOURCE: NASA Goddard Institute for Space Studies", fontsize=10,color='lightgrey')

# Plot 2 settings
ax[1].plot(df2['Year'], df2['SHem'])
ax[1].grid(axis="y")
ax[1].set_ylabel('Temperature')
plt.setp(ax[1].get_xticklabels(), visible=False)
ax[1].tick_params(bottom=True)
ax[1].set_xlim([1880, 2014])

# Plot
g1 = sns.barplot(x="Year", y="SHem", data=df2, ax=ax[0], palette=colors, alpha=.99)
g1 = g1.set(xlabel="Year",
       ylabel="Temperature",
       xticks=[0,20,40,60,80,100,120,134])
