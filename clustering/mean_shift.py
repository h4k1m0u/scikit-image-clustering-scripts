#!/usr/bin/env python
import numpy as np
from sklearn.cluster import estimate_bandwidth, MeanShift
from skimage.filters import threshold_otsu
from geotiff.io import IO


# initialize driver
DIR = 'C:/Data/Tewkesbury-LiDAR'
img = IO.read(DIR + '/stack-lidar.data/Sigma0_HH_slv1_25Jul2007.img')

# mean shift clustering of the image
# cluster pixel intensities using k-means
X = img.reshape((-1, 1))
bandwidth = estimate_bandwidth(X, quantile=.2, n_samples=500)
mean_shift = MeanShift(bandwidth, bin_seeding=True)
mean_shift.fit(X)

# extract means of each cluster & clustered intensities population
clusters_means = mean_shift.cluster_centers_.squeeze()
X_clustered = mean_shift.labels_
print '# of Observations:', X.shape
print 'Means:', clusters_means
print 'Classified:', X_clustered

# get clustered image from clustered intensities
img_clustered = np.choose(X_clustered, clusters_means)
img_clustered.shape = img.shape
IO.write(img_clustered.astype(np.uint8), DIR + '/mean-shift.tif')

# otsu thresholding of the binary image obtained
threshold = threshold_otsu(img_clustered)
img_thresholded = img_clustered > threshold
IO.write(img_thresholded, DIR + '/mean-shift-thresholded.tif')
