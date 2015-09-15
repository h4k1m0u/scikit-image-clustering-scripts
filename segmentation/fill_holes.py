#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal
from skimage.filters import threshold_otsu
from scipy.ndimage.morphology import binary_fill_holes

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

# otsu thresholding of the original image
threshold = threshold_otsu(img)
img_thresholded = img > threshold
print 'Threshold for original image:', threshold

# invert thresholding
not_img_thresholded = np.invert(img_thresholded)
write_image(binary_fill_holes(np.invert(binary_fill_holes(not_img_thresholded))), 'img/test.tif')
