#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
from sklearn.cluster import estimate_bandwidth, MeanShift
from skimage.filters import threshold_otsu

# 1 x 3 grid figure
fig = plt.figure()

# display original image's channel
cell1 = fig.add_subplot(1, 3, 1)
img = io.imread('flood.jpg')[:, :, 0]
io.imshow(img)

# mean shift clustering of the image
# cluster pixel intensities using k-means
cell2 = fig.add_subplot(1, 3, 2)
X = img.reshape((-1, 1))
bandwidth = estimate_bandwidth(X, quantile=.2, n_samples=500)
mean_shift = MeanShift(bandwidth, bin_seeding=True)
mean_shift.fit(X)

# extract means of each cluster & clustered intensities population
clusters_means = mean_shift.cluster_centers_.squeeze()
clustered_X = mean_shift.labels_
print 'Means:', clusters_means
print 'Classified:', clustered_X

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
