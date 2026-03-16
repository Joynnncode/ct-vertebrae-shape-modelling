# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 21:43:15 2024

@author: Joy
"""

import glob  # To list files in a folder
import os    # For file manipulation
import numpy as np

####### Parameters ########
# Adjust these to suit.

folder1 = "../q3dv_tools2023/2"
folder2 = "../q3dv_tools2023/1"
folder3 = "../yjavg"  # Folder to save the averaged points

# Create the new folder if it doesn't exist
os.makedirs(folder3, exist_ok=True)

#### Utility Functions #####
def load_points(path: str):
    """Load points from file.
    Assumes format in which points start on line 4"""
    return np.genfromtxt(path, skip_header=3, skip_footer=1)
# skip_header: The number of lines to skip at the beginning of the file.
# skip_footer: The number of lines to skip at the end of the file.

def save_points(path: str, points: np.ndarray):
    """Save points to file with the same format"""
    header = "version: 1\nn_points: {}\n{{".format(points.shape[0])
    footer = "}"
    np.savetxt(path, points, header=header, footer=footer, comments='')

# Get list of all *.pts files in folder1
filepaths = glob.glob(folder1 + "/*.pts")

n_files = len(filepaths)
print(f"Found {n_files} files in {folder1}")

n_pts = 0  # Will record number of points in each file

n_egs = 0

# Space to store mean distance over all points for example i
per_image_d = np.zeros(n_files)

for i in range(n_files):
    path1 = filepaths[i]

    # Strip the folder name to get the file name
    ptsname = os.path.basename(path1)

    # Construct the path to the equivalent points in folder2
    path2 = os.path.join(folder2, ptsname)

    pts1 = load_points(path1)

    if n_pts == 0:
        n_pts = pts1.shape[0]
        print(f"Expect {n_pts} points in each file, based on {ptsname}")

    if not os.path.isfile(path2):
        print(f"No file {path2} in {folder2}")
        continue

    pts2 = load_points(path2)

    if pts1.shape[0] != n_pts:
        print(f"{path1} has {pts1.shape[0]}")
        continue

    if pts2.shape[0] != n_pts:
        print(f"{path2} has {pts2.shape[0]}")
        continue

    n_egs += 1

    # Compute the average of the points
    avg_pts = (pts1 + pts2) / 2

    # Save the averaged points to the new folder
    avg_path = os.path.join(folder3, ptsname)
    save_points(avg_path, avg_pts)

    #print(f"Averaged points saved to {avg_path}")

print(f"Processed {n_egs} files with averaged points saved in {folder3}")
