# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 13:25:09 2024

@author: Joy
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data from your table
data = {
    'Point': ['mean', 'median', '95%', 'pt 0', 'pt 1', 'pt 2', 'pt 3', 'pt 4', 'pt 5', 'pt 6', 'pt 7', 'pt 8', 'pt 9', 'pt 10', 'pt 11', 'pt 12', 'pt 13', 'pt 14', 'pt 15', 
              'outliers1', 'outliers2', 'outliers3', 'outliers4', 'outliers5'],
    'v1': [1.40, 1.30, 2.30, 1.17, 1.19, 1.13, 1.57, 0.96, 1.20, 1.21, 1.09, 1.64, 1.02, 1.00, 1.33, 2.16, 2.12, 2.01, 2.03, 5.02, 4.57, 3.81, 3.76, 3.66],
    'v2': [1.40, 1.30, 2.20, 1.08, 1.14, 1.11, 1.51, 0.94, 1.15, 1.15, 1.06, 1.56, 0.99, 0.97, 1.28, 2.12, 2.05, 1.98, 2.02, 5.02, 4.57, 3.53, 3.37, 3.26],
    'v3': [1.30, 1.20, 2.00, 1.10, 1.05, 1.07, 1.72, 0.90, 1.12, 1.15, 1.08, 1.43, 1.00, 0.96, 1.26, 1.89, 1.85, 1.84, 1.88, 5.70, 3.69, 3.51, 3.04, 2.96],
    'v4': [1.30, 1.20, 2.00, 1.10, 1.05, 1.05, 1.71, 0.90, 1.10, 1.11, 1.06, 1.43, 1.00, 0.95, 1.23, 1.89, 1.86, 1.84, 1.87, 5.70, 3.51, 3.04, 2.96, 2.70],
    'v5': [1.30, 1.20, 1.90, 1.09, 1.02, 1.04, 1.72, 0.89, 1.06, 1.06, 1.05, 1.42, 0.99, 0.93, 1.19, 1.82, 1.80, 1.77, 1.83, 2.96, 2.70, 2.64, 2.44, 2.23]



}

# Creating a DataFrame
df = pd.DataFrame(data)

# Filtering out the rows that are not specific points
point_data = df[~df['Point'].isin(['mean', 'median', '95%'])].copy()

# Converting the data from wide to long format for easier plotting
long_df = pd.melt(point_data, id_vars=['Point'], var_name='Version', value_name='Difference')

# # Plotting boxplots
# plt.figure(figsize=(5, 3))
# sns.boxplot(x='Version', y='Difference', palette="Set3", data=long_df)
# plt.title('Distribution of Differences Across Versions(YJ1 vs. YJ2)')
# plt.ylabel('Difference (mm)')
# plt.show()

# Plotting line plots for each point across versions
# plt.figure(figsize=(12, 8))
# sns.lineplot(x='Version', y='Difference', hue='Point', data=long_df, marker='o')
# plt.title('Difference for Each Point Across Versions')
# plt.ylabel('Difference (mm)')
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.show()
# 绘制各点与各版本之间差异的热图（不包含outliers）
# 过滤掉outliers数据
filtered_df = df[~df['Point'].str.contains('outliers') & ~df['Point'].isin(['mean', 'median', '95%'])].copy()


heatmap_data = filtered_df.set_index('Point').T
plt.figure(figsize=(8, 4))
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Heatmap (HX1 vs. YJ1)', fontsize=20,  pad=20, loc='center')
plt.ylabel('Versions',fontsize=20)
plt.xlabel('Points',fontsize=20)
plt.show()