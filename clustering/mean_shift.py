#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal
from sklearn.cluster import estimate_bandwidth, MeanShift
from skimage.filters import threshold_otsu

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

# mean shift clustering of the image
# cluster pixel intensities using k-means
X = img.reshape((-1, 1))
bandwidth = estimate_bandwidth(X, quantile=.2, n_samples=500)
mean_shift = MeanShift(bandwidth, bin_seeding=True)
mean_shift.fit(X)

# extract means of each cluster & clustered intensities population
clusters_means = mean_shift.cluster_centers_.squeeze()
X_clustered = mean_shift.labels_
print '# of Observations:', X.shape
print 'Means:', clusters_means
print 'Classified:', clustered_X

# get clustered image from clustered intensities
img_clustered = np.choose(X_clustered, clusters_means)
img_clustered.shape = img.shape
write_image(img_clustered.astype(np.uint8), '../img/mozambique-after-subset-mean-shift.tiff')

# otsu thresholding of the binary image obtained
threshold = threshold_otsu(img_clustered)
img_thresholded = img_clustered > threshold
write_image(img_thresholded, '../img/mozambique-after-subset-mean-shift-thresholded.tiff')
