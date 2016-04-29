#!/usr/bin/env python
import numpy as np
from skimage.feature import local_binary_pattern
import skimage.io as io
from sklearn import cluster

# read image
img = io.imread('/home/hakim/Github/matlab-segmentation/myanmar.png', as_grey=True)
io.imshow(img)
io.show()

# extract texture using local binary pattern
img_texture = local_binary_pattern(img, P=16, R=16, method='ror')
io.imshow(img_texture)
io.show()

# cluster texture using k-means
X = img_texture.reshape((-1, 1))
k_means = cluster.KMeans(n_clusters=2)
k_means.fit(X)

# clustered intensities population
X_clustered = k_means.labels_

# get clustered image from clustered intensities
img_clustered = np.choose(X_clustered, [255, 0])
img_clustered.shape = img.shape
io.imshow(np.invert(img_clustered))
io.show()
