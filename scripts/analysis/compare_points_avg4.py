# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 21:58:48 2024

@author: Joy
"""


import glob  # To list files in a folder
import os    # For file manipulation
import numpy as np

####### Parameters ########
# Adjust these to suit.

folders = ["../q3dv_tools2023/points_hx1", "../q3dv_tools2023/points_hx2", 
           "../q3dv_tools2023/1", "../q3dv_tools2023/2"]
output_folder = "../points_avg"  # Folder to save the averaged points

# Create the new folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

#### Utility Functions #####
def load_points(path: str):
    """Load points from file. Assumes format in which points start on line 4"""
    return np.genfromtxt(path, skip_header=3, skip_footer=1)
# skip_header: The number of lines to skip at the beginning of the file.
# skip_footer: The number of lines to skip at the end of the file.

def save_points(path: str, points: np.ndarray):
    """Save points to file with the same format"""
    header = "version: 1\nn_points: {}\n{{".format(points.shape[0])
    footer = "}"
    np.savetxt(path, points, header=header, footer=footer, comments='')

# Get list of all *.pts files in the first folder
filepaths = glob.glob(folders[0] + "/*.pts")

n_files = len(filepaths)
print(f"Found {n_files} files in {folders[0]}")

n_pts = 0  # Will record number of points in each file

n_egs = 0

for i in range(n_files):
    path1 = filepaths[i]
    
    # Strip the folder name to get the file name
    ptsname = os.path.basename(path1)
    
    points = []
    valid_file = True
    
    for folder in folders:
        path = os.path.join(folder, ptsname)
        if not os.path.isfile(path):
            print(f"No file {path} in {folder}")
            valid_file = False
            break
        
        pts = load_points(path)
        if n_pts == 0:
            n_pts = pts.shape[0]
            print(f"Expect {n_pts} points in each file, based on {ptsname}")
        
        if pts.shape[0] != n_pts:
            print(f"{path} has {pts.shape[0]} points instead of {n_pts}")
            valid_file = False
            break
        
        points.append(pts)
    
    if not valid_file:
        continue
    
    n_egs += 1
    
    # Compute the average of the points
    avg_pts = np.mean(points, axis=0)
    
    # Save the averaged points to the new folder
    avg_path = os.path.join(output_folder, ptsname)
    save_points(avg_path, avg_pts)
    
    #print(f"Averaged points saved to {avg_path}")

print(f"Processed {n_egs} files with averaged points saved in {output_folder}")
