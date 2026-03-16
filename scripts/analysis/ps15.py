# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 14:15:05 2024

@author: Joy
"""

import matplotlib.pyplot as plt

# Data for the experiment with patch size 15x15x15
frame_widths = [20, 30, 40, 50, 60]
mean_distances = [2.16, 1.7, 1.64, 1.71, 1.8]
standard_errors = [0.0146, 0.0128, 0.0128, 0.0136, 0.015]
standard_deviations = [0.873, 0.767, 0.764, 0.816, 0.895]
medians = [1.98, 1.53, 1.49, 1.55, 1.58]
percentile_90 = [3.09, 2.52, 2.49, 2.59, 2.81]
percentile_95 = [4.06, 3.04, 2.98, 3.15, 3.4]
percentile_99 = [5.45, 4.73, 4.59, 4.87, 5.11]
search_times = [55, 65.9, 130, 169, 162]

# Create subplots for each metric
fig, axs = plt.subplots(2, 2, figsize=(9, 9))

# Mean Distance vs Frame Width
axs[0, 0].plot(frame_widths, mean_distances, marker='o', color='m')
axs[0, 0].plot(frame_widths, medians, marker='o',  color='olive')
axs[0, 0].set_title('Mean & Median vs. Frame Width')
axs[0, 0].set_xlabel('Frame Width')
axs[0, 0].set_ylabel('Mean & Median')

# Standard Error vs Frame Width
axs[1, 1].plot(frame_widths, standard_errors, marker='o', color='purple')
axs[1, 1].set_title('Standard Error vs. Frame Width')
axs[1, 1].set_xlabel('Frame Width')
axs[1, 1].set_ylabel('Standard Error')

# Standard Deviation vs Frame Width
axs[1, 0].plot(frame_widths, standard_deviations, marker='o', color='blue')
axs[1, 0].set_title('Standard Deviation vs. Frame Width')
axs[1, 0].set_xlabel('Frame Width')
axs[1, 0].set_ylabel('Standard Deviation')

# Median vs Frame Width
# axs[1, 1].plot(frame_widths, medians, marker='o', color='b')
# axs[1, 1].set_title('Median vs. Frame Width')
# axs[1, 1].set_xlabel('Frame Width')
# axs[1, 1].set_ylabel('Median Distance')

# Percentiles vs Frame Width
axs[0, 1].plot(frame_widths, percentile_90, marker='o', label='90th Percentile', color='c')
axs[0, 1].plot(frame_widths, percentile_95, marker='o', label='95th Percentile', color='orange')
axs[0, 1].plot(frame_widths, percentile_99, marker='o', label='99th Percentile', color='g')
axs[0, 1].set_title('Percentiles vs. Frame Width')
axs[0, 1].set_xlabel('Frame Width')
axs[0, 1].set_ylabel('Percentile Distance')
axs[0, 1].legend()


# Adjust layout
plt.tight_layout()
plt.show()
