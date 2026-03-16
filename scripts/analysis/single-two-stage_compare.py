# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:00:10 2024

@author: Joy
"""

import matplotlib.pyplot as plt
import numpy as np

# New data from the experiments
patch_sizes = ['12x12x12', '13x13x13', '14x14x14', '15x15x15', '16x16x16']
mean_distance_1 = [1.71, 1.68, 1.67, 1.64, 1.64]  # Data for the first set of experiments
mean_distance_2 = [1.65, 1.65, 1.65, 1.65, 1.65]  # Data for the second set of experiments

# Width of the bars
bar_width = 0.35

# Set up the positions of the bars on the x-axis
r1 = np.arange(len(patch_sizes))
r2 = [x + bar_width for x in r1]

# Create the bar chart with different colors
plt.figure(figsize=(8, 6))
bars1 = plt.bar(r1, mean_distance_1, color='pink', width=bar_width, edgecolor='grey', label='Single Model')
bars2 = plt.bar(r2, mean_distance_2, color='yellow', width=bar_width, edgecolor='grey', label='Two-Stage Model')

# Add the value labels above the bars
def add_value_labels(bars):
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 0.02,  # Adjusted position to be slightly above the bar
                 f'{height:.2f}',  # Format the number to 2 decimal places
                 ha='center',  # Horizontal alignment: center
                 va='bottom',  # Vertical alignment: bottom
                 fontsize=10)  # Font size for the label

add_value_labels(bars1)
add_value_labels(bars2)

# Add labels and title
plt.xlabel('Patch Size', fontweight='bold')
plt.ylabel('Final Mean Distance (mm)',fontweight='bold')
plt.xticks([r + bar_width / 2 for r in range(len(patch_sizes))], patch_sizes)
plt.title('Comparison of Final Mean Distance for Different Patch Sizes')

# Set y-axis limit
plt.ylim(0, 2)  # Set y-axis from 0 to 2

# Show the plot
plt.legend()
plt.show()
