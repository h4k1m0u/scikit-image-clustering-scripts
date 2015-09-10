#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.filters import threshold_otsu
from sklearn import cluster

# 1 x 2 grid figure
fig = plt.figure()

# display original image's channel
cell1 = fig.add_subplot(1, 3, 1)
img = io.imread('flood.jpg')[:, :, 0]
io.imshow(img)

# k-means clustering of the image (population of pixels intensities)
# cluster pixel intensities using k-means
cell2 = fig.add_subplot(1, 3, 2)
X = img.reshape((-1, 1))
k_means = cluster.KMeans(n_clusters=5)
k_means.fit(X)

# extract means of each cluster & clustered intensities population
clusters_means = k_means.cluster_centers_.squeeze()
clustered_X = k_means.labels_

# get clustered image from clustered intensities
clustered_img = np.choose(clustered_X, clusters_means)
clustered_img.shape = img.shape
io.imshow(clustered_img.astype(np.uint8))

# otsu thresholding of the binary image obtained
cell3 = fig.add_subplot(1, 3, 3)
threshold = threshold_otsu(clustered_img)
thresholded_img = clustered_img > threshold
io.imshow(thresholded_img)

# show figure grid
plt.show()
