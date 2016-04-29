#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal
import skimage.io as io
from sklearn import cluster

# initialize driver
driver = gdal.GetDriverByName('GTiff')

def write_image(img, filename):
    """
    Write img array to a file with the given filename
    Args:
        img (Band)
        filename (str)
    """
    x_size = img.shape[1]
    y_size = img.shape[0]
    dataset = driver.Create(filename, x_size, y_size)
    dataset.GetRasterBand(1).WriteArray(img)

# load original image
dataset = gdal.Open('/home/hakim/Data/Rakhine-Myanmar/during/postimage-subset.data/Sigma0_VV.img')
band = dataset.GetRasterBand(1)
img = band.ReadAsArray().astype(np.float64)
w = img.shape[1]
h = img.shape[0]

# spatial dimensions
X = np.tile(np.arange(w), (h, 1))
Y = np.tile(np.arange(h), (w, 1)).T

# create feature set
X = X.flatten()
Y = Y.flatten()
I = img.flatten()
S = np.concatenate((I[:, np.newaxis], X[:, np.newaxis], Y[:, np.newaxis]), axis=1)

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
write_image(img_clustered, 'img/rahkine-clustered.tif')
