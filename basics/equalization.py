#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal
from skimage.filters import threshold_otsu
from skimage.exposure import equalize_hist

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
dataset = gdal.Open('../img/flood.jpg')
band = dataset.GetRasterBand(1)
img = band.ReadAsArray().astype(np.uint8)

# histogram-equalization of the image (enhance contrast)
img_equalized = equalize_hist(img)
write_image(img_equalized, 'img/mozambique-after-thresholded.tiff')

# otsu thresholding of the image
threshold = threshold_otsu(img_equalized)
img_equalized_thresholded = img_equalized > threshold
print 'Threshold:', int(255 * threshold)
write_image(img_equalized_thresholded, 'img/mozambique-after-thresholded-equalized.tiff')
