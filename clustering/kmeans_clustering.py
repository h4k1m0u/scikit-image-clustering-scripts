#!/usr/bin/env python
import numpy as np
from skimage.filters import threshold_otsu
from sklearn import cluster
from geotiff.io import IO


# load original image
DIR = 'C:/Data/Tewkesbury-LiDAR'
img = IO.read(DIR + '/stack-lidar.data/Sigma0_HH_slv1_25Jul2007.img')

# k-means clustering of the image (population of pixels intensities)
# cluster pixel intensities using k-means
X = img.reshape((-1, 1))
k_means = cluster.KMeans(n_clusters=2)
k_means.fit(X)

# extract means of each cluster & clustered intensities population
clusters_means = k_means.cluster_centers_.squeeze()
X_clustered = k_means.labels_
print '# of Observations:', X.shape
print 'Clusters Means:', clusters_means

# get clustered image from clustered intensities
img_clustered = np.choose(X_clustered, (0, 1))
img_clustered.shape = img.shape
IO.write(img_clustered, DIR + '/kmeans.tif')

# otsu thresholding of the binary image obtained
threshold = threshold_otsu(img_clustered)
img_thresholded = img_clustered > threshold
IO.write(img_thresholded, DIR + '/kmeans-thresholding.tif')
