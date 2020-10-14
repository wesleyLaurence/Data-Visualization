"""
Sources of added sugar in United States diet
Data Source: https://health.gov/our-work/food-nutrition/2015-2020-dietary-guidelines/guidelines/
Chart created by Wesley Laurence
"""

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_excel('added-sugar-dataset.xlsx')

# Set font family
plt.rcParams["font.family"] = "Arial"

# Create pie chart
labels = 'Snacks & Sweets', 'Beverages (not milk or 100% fruit juice)', 'Other Sources'
sizes = [31, 47, 22]
explode = (0, 0, 0.08)  # only "explode" the 2nd slice (i.e. 'Hogs')

# Color settings
color_list = ['red','tomato','lightgray']

# Create plot
fig1, ax1 = plt.subplots(figsize=(12,12))
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, explode=explode, startangle=90, colors = color_list,textprops={'fontsize': 19})
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title("Sources of Added Sugars in the U.S Population \nAges 2 Years & Older", fontweight='bold',fontsize=23, fontname="Arial")

# Set data source label
ax1.text(-.65, -1.3, r"DATA SOURCE: 2015-2020 Dietary Guidelines for Americans", fontsize=14,color='grey')

# Show plot
plt.show()
