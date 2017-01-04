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
img_clustered = g.predict(X)
img_clustered.shape = img.shape
img_clustered = img_clustered.astype(np.float)

# save clustered image
IO.write(img_clustered, DIR + '/gmm.tif')

# image size
img_gmm = np.empty_like(img_clustered)
img_gmm[:] = img_clustered
l = img_clustered.shape[1]
h = img_clustered.shape[0]

# consider neighbourhood during clustering
step = 1
for i in xrange(1, h-1):
    for j in xrange(1, l-1):
        # counts of #elems/cluster in the neighbourhood
        c, f = np.unique(img_clustered[i-step:i+step+1, j-step:j+step+1],
                         return_counts=True)
        freqs = dict(zip(c, f))

        # switch to the majority cluster in the neighbourhood
        try:
            if img_clustered[i, j] != 0.0 and freqs[0.0] > 4:
                img_clustered[i, j] = 0.0
            elif img_clustered[i, j] != 1.0 and freqs[1.0] > 4:
                img_clustered[i, j] = 1.0
        except KeyError, e:
            pass

# show clustered image with spatial context
print 'Eqality test:', (img_gmm == img_clustered).all()
IO.write(img_clustered, DIR + '/gmm-spatial.tif')
