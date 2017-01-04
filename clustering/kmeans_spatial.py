#!/usr/bin/env python
import numpy as np
from sklearn import cluster
from geotiff.io import IO


# load original image
DIR = 'C:/Data/Tewkesbury-LiDAR'
img = IO.read(DIR + '/stack-lidar.data/Sigma0_HH_slv1_25Jul2007.img')
w = img.shape[1]
h = img.shape[0]

# spatial dimensions
X = np.tile(np.arange(w), (h, 1))
Y = np.tile(np.arange(h), (w, 1)).T

# create feature set
X = X.flatten()
Y = Y.flatten()
I = img.flatten()
S = np.concatenate((I[:, np.newaxis], X[:, np.newaxis], Y[:, np.newaxis]),
                   axis=1)

# normalize features
mean = np.mean(S, axis=0)
std = np.std(S, axis=0, ddof=1)
S = (S - mean) / std

# clustering
k_means = cluster.KMeans(n_clusters=2)
k_means.fit(S)

# extract means of each cluster & clustered intensities population
clusters_means = k_means.cluster_centers_.squeeze()
clusters = k_means.labels_

# get clustered image from clustered intensities
img_clustered = np.choose(clusters, [0.0, 1.0])
img_clustered.shape = img.shape
IO.write(img_clustered, DIR + '/kmeans-spatial.tif')
