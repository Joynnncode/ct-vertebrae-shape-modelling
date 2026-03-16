# -*- coding: utf-8 -*-
"""
Tool to compare points in two different folders.
Lists all points files (*.pts) in one folder.
If there is a file with the same name in the other folder it
loads in the points and compares them.

"""

import glob  # To list files in a folder
import os    # For file manipulation
import numpy as np

####### Parameters ########
# Adjust these to suit.

# folder1="../version8(avg4)/points_avg"
folder1="../version6/points_YJ2"
folder2="../version8(avg4)/points_avg"
# folder2="../version7(avg2)/yjavg"
# folder1="../output/avg_test"
# # folder2="../output/single/output_points40(12)"
# folder2="../output/fw30/output_points1515"


#### Utility Functions #####
def load_points(path : str):
    """Load points from file.
    Assumes format in which points start on line 4"""
    return np.genfromtxt(path,skip_header=3,skip_footer=1)


def summary_stats(x):
    """Return string of summary statistics"""
    s= f" mean: {x.mean():.1f}"
    s+=f" median: {np.median(x):.1f}"
    s+=f" 95%: {np.percentile(x,95):.1f}"
    return s
    

# Get list of all *.pts files in folder1
filepaths=glob.glob(folder1+"/*.pts")

n_files=len(filepaths)
print(f"Found {n_files} files in {folder1}")

n_pts=0 # Will record number of points in each file

n_egs=0

# Space to store mean distance over all points for example i
per_image_d=np.zeros(n_files)

for i in range(n_files): 
    path1=filepaths[i]
    
    # Strip the folder name to get the file name
    ptsname=os.path.basename(path1)
    
    # Construct the path to the equivalent points in folder2
    path2=folder2+"/"+ptsname
    # path2 = os.path.join(folder2, ptsname + '.v3i.pts')
    
    pts1=load_points(path1)
    
    if n_pts==0:
        n_pts=pts1.shape[0]
        print(f"Expect {n_pts} points in each file, based on {ptsname}")
    
    if not os.path.isfile(path2):
        print(f"No file {path2} in {folder2}")
        continue

    pts2=load_points(path2)
    
    if pts1.shape[0] != n_pts:
        print(f"{path1} has {pts1.shape[0]}")
        continue
    
    if pts2.shape[0] != n_pts:
        print(f"{path2} has {pts2.shape[0]}")
        continue
    
    n_egs+=1
    
    # Compute the difference between the points
    dpts=pts2-pts1
    
    dpts_sqr=np.square(dpts)
    
    # Compute distance for each point
    # sqrt(sum of squares of each row)
    d=np.sqrt(dpts_sqr.sum(axis=1))
        
    if n_egs==1:
        sum_dpts=dpts
        sum_d=d
    else:
        sum_dpts+=dpts
        sum_d+=d
        
    per_image_d[i]=d.mean()
    
# Mean displacement in x,y,z
mean_dpts=sum_dpts/n_egs

# Mean distance between points
mean_d=sum_d/n_egs

print(f"Overall mean distance between points: {summary_stats(per_image_d)}")
print("Mean displacement per point:")
for i in range(n_pts):
    print(f"Pt {i} : {mean_d[i]:.2f}")
    
# per_image_d[i] gives mean displacement for example i
# Look at the worst few cases
index=np.argsort(per_image_d)
index=np.flip(index) # Largest first
for j in range(5):
    print(f"{filepaths[index[j]]} mean_d={per_image_d[index[j]]:.2f}")