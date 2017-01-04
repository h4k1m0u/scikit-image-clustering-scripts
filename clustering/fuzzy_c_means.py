#!/usr/bin/env python
import numpy as np
import skfuzzy as fuzz
from geotiff.io import IO


# load original image
DIR = 'C:/Data/Tewkesbury-LiDAR'
img = IO.read(DIR + '/stack-lidar.data/Sigma0_HH_slv1_25Jul2007.img')

# pixel intensities
I = img.reshape((1, -1))

# params
n_centers = 2
fuzziness_degree = 2
error = 0.005
maxiter = 1000

# fuzz c-means clustering
centers, u, u0, d, jm, n_iters, fpc = fuzz.cluster.cmeans(
    I,
    c=n_centers,
    m=fuzziness_degree,
    error=error,
    maxiter=maxiter,
    init=None
)
img_clustered = np.argmax(u, axis=0).astype(float)

# display clusters
img_clustered.shape = img.shape
IO.write(img_clustered, DIR + '/fuzzy-clustered.tif')
