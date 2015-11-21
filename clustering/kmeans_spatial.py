#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu
import skimage.io as io
from sklearn import cluster

# load original image
img = io.imread('myanmar.png', as_grey=True)
w = img.shape[1]
h = img.shape[0]

# spatial dimensions
X = np.tile(np.arange(w), (w, 1))
Y = X.T
X = X.reshape((-1, 1)).flatten()
Y = Y.reshape((-1, 1)).flatten()

# pixel intensities
I = img.reshape((-1, 1)).flatten()

# clustering
O = np.concatenate((I[:, np.newaxis], X[:, np.newaxis], Y[:, np.newaxis]), axis=1)
k_means = cluster.KMeans(n_clusters=2)
k_means.fit(O)

# extract means of each cluster & clustered intensities population
clusters_means = k_means.cluster_centers_.squeeze()
clusters = k_means.labels_

# get clustered image from clustered intensities
img_clustered = np.choose(clusters, [0.0, 1.0])
img_clustered.shape = img.shape
io.imshow(img_clustered)
io.show()
