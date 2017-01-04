#!/usr/bin/env python
import numpy as np
from sklearn import mixture
from geotiff.io import IO


# load original image
DIR = 'C:/Data/Tewkesbury-LiDAR'
img = IO.read(DIR + '/stack-lidar.data/Sigma0_HH_slv1_25Jul2007.img')

# gaussian mixture model
# fit gaussian mixture model to the pixel intensities observation
X = img.reshape((-1, 1))
g = mixture.GMM(n_components=2)
g.fit(X)
print '# of Observations:', X.shape
print 'Gaussian Weights:', g.weights_
print 'Gaussian Means:', g.means_

# predict classes of pixel intensities from normal gmm
img_clustered1 = g.predict(X)
img_clustered1.shape = img.shape
img_clustered1 = img_clustered1.astype(np.float)
IO.write(img_clustered1, DIR + '/gmm.tif')

# predict classes of pixel intensities by thresholding the gmm probabilities
img_clustered2 = g.predict_proba(X)
img_clustered2 = np.array(map(lambda x: False if x[1] > 0.1 else True,
                              img_clustered2))
img_clustered2.shape = img.shape
IO.write(img_clustered2, DIR + '/gmm-empirical.tif')

# thresholding using average of estimated gaussian means
threshold = np.average(g.means_)
print 'Gaussian Means Average:', threshold
img_thresholded = img > threshold
IO.write(img_thresholded, DIR + '/gmm-thresholding.tif')
