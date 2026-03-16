# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 14:13:30 2024

@author: Joy
"""

import matplotlib.pyplot as plt

# Data for the experiment with frame width 40
patch_sizes = ['12', '13', '14', '15', '16']
mean_distances = [1.71, 1.68, 1.67, 1.64, 1.64]
standard_errors = [0.013, 0.0128, 0.0126, 0.0128, 0.0125]
standard_deviations = [0.777, 0.764, 0.753, 0.764, 0.75]
medians = [1.55, 1.52, 1.52, 1.49, 1.48]
percentile_90 = [2.59, 2.54, 2.55, 2.49, 2.5]
percentile_95 = [3.08, 3.01, 3.06, 2.98, 3]
percentile_99 = [4.5, 4.4, 4.44, 4.59, 4.61]
search_times = [118, 112, 91.7, 130, 98]

# Create subplots for each metric
fig, axs = plt.subplots(2, 2, figsize=(9, 9))

# Mean Distance vs Patch Size
axs[0, 0].plot(patch_sizes, mean_distances, marker='o', color='m')
axs[0, 0].plot(patch_sizes, medians, marker='o',  color='olive')
axs[0, 0].set_title('Mean & Median vs. Patch Size')
axs[0, 0].set_xlabel('Patch Size')
axs[0, 0].set_ylabel('Mean & Median')

# Standard Error vs Patch Size
axs[1, 1].plot(patch_sizes, standard_errors, marker='o', color='purple')
axs[1, 1].set_title('Standard Error vs. Patch Size')
axs[1, 1].set_xlabel('Patch Size')
axs[1, 1].set_ylabel('Standard Error')

# Standard Deviation vs Patch Size
axs[1, 0].plot(patch_sizes, standard_deviations, marker='o', color='blue')
axs[1, 0].set_title('Standard Deviation vs. Patch Size')
axs[1, 0].set_xlabel('Patch Size')
axs[1, 0].set_ylabel('Standard Deviation')

# Median vs Patch Size
# axs[1, 1].plot(patch_sizes, medians, marker='o', color='b')
# axs[1, 1].set_title('Median vs. Patch Size')
# axs[1, 1].set_xlabel('Patch Size')
# axs[1, 1].set_ylabel('Median Distance')

# Percentiles vs Patch Size
axs[0, 1].plot(patch_sizes, percentile_90, marker='o', label='90th Percentile', color='c')
axs[0, 1].plot(patch_sizes, percentile_95, marker='o', label='95th Percentile', color='orange')
axs[0, 1].plot(patch_sizes, percentile_99, marker='o', label='99th Percentile', color='g')
axs[0, 1].set_title('Percentiles vs. Patch Size')
axs[0, 1].set_xlabel('Patch Size')
axs[0, 1].set_ylabel('Percentile Distance')
axs[0, 1].legend()


# Adjust layout
plt.tight_layout()
plt.show()
