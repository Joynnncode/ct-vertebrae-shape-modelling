# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 13:57:29 2024

@author: Joy
"""
import matplotlib.pyplot as plt

# Data
frame_widths = [20, 30, 40, 50, 60, 70]
mean_distance = [2.16, 1.72, 1.67, 1.73, 1.82, 1.93]
standard_error = [0.0142, 0.0127, 0.0126, 0.0138, 0.0147, 0.0167]
std_dev = [0.852, 0.762, 0.753, 0.824, 0.879, 0.997]
median = [1.97, 1.54, 1.52, 1.56, 1.63, 1.69]
percentile_90 = [3.13, 2.53, 2.55, 2.66, 2.8, 3.1]
percentile_95 = [3.84, 3.17, 3.06, 3.13, 3.32, 3.82]
percentile_99 = [5.38, 4.59, 4.44, 5.19, 5.24, 5.8]
search_time = [48.6, 86.2, 91.7, 154, 198, 449]

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(9, 9))

axs[0, 0].plot(frame_widths, mean_distance, marker='o', color='m')
axs[0, 0].plot(frame_widths, median, marker='o', color = 'olive')
axs[0, 0].set_title('Mean & Median vs. Frame Width')
axs[0, 0].set_xlabel('Frame Width')
axs[0, 0].set_ylabel('Mean & Median')

axs[1, 1].plot(frame_widths, standard_error, marker='o', color='purple' )
axs[1, 1].set_title('Standard Error vs. Frame Width')
axs[1, 1].set_xlabel('Frame Width')
axs[1, 1].set_ylabel('Standard Error')

axs[1, 0].plot(frame_widths, std_dev, marker='o',color='olive' )
axs[1, 0].set_title('Standard Deviation vs. Frame Width')
axs[1, 0].set_xlabel('Frame Width')
axs[1, 0].set_ylabel('Standard Deviation')


axs[0, 1].plot(frame_widths, percentile_90, marker='o', label='90th Percentile')
axs[0, 1].plot(frame_widths, percentile_95, marker='o', label='95th Percentile')
axs[0, 1].plot(frame_widths, percentile_99, marker='o', label='99th Percentile')
axs[0, 1].set_title('Percentiles vs. Frame Width')
axs[0, 1].set_xlabel('Frame Width')
axs[0, 1].set_ylabel('Percentile Distance')
axs[0, 1].legend()


plt.tight_layout()
plt.show()

