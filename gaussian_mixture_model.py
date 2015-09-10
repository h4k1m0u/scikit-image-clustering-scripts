#!/usr/bin/env python
import matplotlib.pyplot as plt
import skimage.io as io
from sklearn import mixture
import numpy as np

# 1 x 2 grid figure
fig = plt.figure()

# display original image's channel
cell1 = fig.add_subplot(2, 2, 1)
img = io.imread('flood.jpg')[:, :, 0]
io.imshow(img)

# gaussian mixture model
# fit gaussian mixture model to the pixel intensities observation
X = img.reshape((-1, 1))
g = mixture.GMM(n_components=2)
g.fit(X)
print 'Gaussian Weights:', g.weights_
print 'Gaussian Means:', g.means_

# predict classes of pixel intensities from normal gmm
cell2 = fig.add_subplot(2, 2, 2)
clustered_img1 = g.predict(X)
clustered_img1.shape = img.shape
clustered_img1 = clustered_img1.astype(np.float)
io.imshow(clustered_img1)

# predict classes of pixel intensities by thresholding the gmm map of probabilities
cell3 = fig.add_subplot(2, 2, 3)
clustered_img2 = g.predict_proba(X)
clustered_img2 = np.array(map(lambda x: False if x[1] > 0.1 else True, clustered_img2))
clustered_img2.shape = img.shape
io.imshow(clustered_img2)

# thresholding using average of estimated gaussian means
cell4 = fig.add_subplot(2, 2, 4)
threshold = np.average(g.means_)
print 'Gaussian Means Average:', threshold
thresholded_img = img > threshold
io.imshow(thresholded_img)

# show figure grid
plt.show()
