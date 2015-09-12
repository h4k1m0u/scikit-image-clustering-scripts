#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal
from skimage.filters import threshold_otsu
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
dataset = gdal.Open('../img/mozambique-after-subset.tiff')
band = dataset.GetRasterBand(1)
img = band.ReadAsArray().astype(np.uint8)

# k-means clustering of the image (population of pixels intensities)
# cluster pixel intensities using k-means
X = img.reshape((-1, 1))
k_means = cluster.KMeans(n_clusters=5)
k_means.fit(X)

# extract means of each cluster & clustered intensities population
clusters_means = k_means.cluster_centers_.squeeze()
X_clustered = k_means.labels_
print '# of Observations:', X.shape
print 'Clusters Means:', clusters_means

# get clustered image from clustered intensities
img_clustered = np.choose(X_clustered, clusters_means)
img_clustered.shape = img.shape
write_image(img_clustered, '../img/mozambique-after-subset-kmeans.tiff')

# otsu thresholding of the binary image obtained
threshold = threshold_otsu(img_clustered)
img_thresholded = img_clustered > threshold
write_image(img_thresholded, '../img/mozambique-after-subset-kmeans-thresholding.tiff')
