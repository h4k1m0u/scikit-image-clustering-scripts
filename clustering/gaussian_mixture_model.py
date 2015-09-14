#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal
from sklearn import mixture

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
dataset = gdal.Open('img/mozambique-after-subset.tif')
band = dataset.GetRasterBand(1)
img = band.ReadAsArray().astype(np.uint8)

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
img_clustered1  = img_clustered1.astype(np.float)
write_image(img_clustered1, 'img/mozambique-after-subset-gmm.tif')

# predict classes of pixel intensities by thresholding the gmm map of probabilities
img_clustered2 = g.predict_proba(X)
img_clustered2 = np.array(map(lambda x: False if x[1] > 0.1 else True, img_clustered2))
img_clustered2.shape = img.shape
write_image(img_clustered2, 'img/mozambique-after-subset-gmm-empirical.tif')

# thresholding using average of estimated gaussian means
threshold = np.average(g.means_)
print 'Gaussian Means Average:', threshold
img_thresholded = img > threshold
write_image(img_thresholded, 'img/mozambique-after-subset-gmm-thresholding.tif')
