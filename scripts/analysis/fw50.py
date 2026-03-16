# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:19:25 2024

@author: Joy
"""

import matplotlib.pyplot as plt

# Data
patch_sizes = ['5', '6', '7', '8', '10', '12', '13', '14', '15', '16']
mean_distance = [2.3, 2.2, 2.07, 1.97, 1.85, 1.85, 1.77, 1.75, 1.71, 1.71]
standard_error = [0.015, 0.0148, 0.0145, 0.0144, 0.0142, 0.0138, 0.014, 0.0138, 0.0136, 0.0137]
std_dev = [0.897, 0.885, 0.866, 0.859, 0.85, 0.828, 0.835, 0.825, 0.816, 0.819]
median = [2.14, 2.03, 1.92, 1.8, 1.67, 1.67, 1.6, 1.56, 1.55, 1.53]
percentile_90 = [3.45, 3.23, 3.16, 2.99, 2.82, 2.89, 2.72, 2.69, 2.59, 2.65]
percentile_95 = [3.99, 3.82, 3.65, 3.48, 3.27, 3.31, 3.22, 3.2, 3.15, 3.17]
percentile_99 = [5.37, 5.54, 5.24, 5.27, 4.91, 4.84, 5.06, 4.61, 4.87, 4.83]
# search_time = [278, 346, 351, 326, 303, 144, 174, 176, 169, 177]

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(9, 9))

axs[0, 0].plot(patch_sizes, mean_distance, marker='o',  color='m')
axs[0, 0].plot(patch_sizes, median, marker='o',  color='olive')
axs[0, 0].set_title('Mean & Median vs. Patch Size')
axs[0, 0].set_xlabel('Patch Size')
axs[0, 0].set_ylabel('Mean & Median')

axs[1, 1].plot(patch_sizes, standard_error, marker='o', color='purple')
axs[1, 1].set_title('Standard Error vs. Patch Size')
axs[1, 1].set_xlabel('Patch Size')
axs[1, 1].set_ylabel('Standard Error')

axs[1, 0].plot(patch_sizes, std_dev, marker='o', color='blue')
axs[1, 0].set_title('Standard Deviation vs. Patch Size')
axs[1, 0].set_xlabel('Patch Size')
axs[1, 0].set_ylabel('Standard Deviation')

# axs[1, 1].plot(patch_sizes, median, marker='o')
# axs[1, 1].set_title('Median vs. Patch Size')
# axs[1, 1].set_xlabel('Patch Size')
# axs[1, 1].set_ylabel('Median Distance')

axs[0, 1].plot(patch_sizes, percentile_90, marker='o', label='90th Percentile')
axs[0, 1].plot(patch_sizes, percentile_95, marker='o', label='95th Percentile')
axs[0, 1].plot(patch_sizes, percentile_99, marker='o', label='99th Percentile')
axs[0, 1].set_title('Percentiles vs. Patch Size')
axs[0, 1].set_xlabel('Patch Size')
axs[0, 1].set_ylabel('Percentile Distance')
axs[0, 1].legend()

# axs[2, 1].plot(patch_sizes, search_time, marker='o', color='r')
# axs[2, 1].set_title('Search Mean Time vs. Patch Size')
# axs[2, 1].set_xlabel('Patch Size')
# axs[2, 1].set_ylabel('Search Mean Time (ms)')

plt.tight_layout()
plt.show()
