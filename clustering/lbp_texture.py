#!/usr/bin/env python
import numpy as np
from skimage.feature import local_binary_pattern
from sklearn import cluster
from geotiff.io import IO


# read image
DIR = 'C:/Data/Tewkesbury-LiDAR'
img = IO.read(DIR + '/stack-lidar.data/Sigma0_HH_slv1_25Jul2007.img')

# extract texture using local binary pattern
img_texture = local_binary_pattern(img, P=16, R=16, method='ror')
IO.write(img_texture, DIR + '/texture.tif')

# cluster texture using k-means
X = img_texture.reshape((-1, 1))
k_means = cluster.KMeans(n_clusters=2)
k_means.fit(X)

# clustered intensities population
X_clustered = k_means.labels_

# get clustered image from clustered intensities
img_clustered = np.choose(X_clustered, [255, 0])
img_clustered.shape = img.shape
IO.write(np.invert(img_clustered), DIR + '/texture-clustered.tif')
