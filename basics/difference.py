#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal
from skimage.transform import resize
from skimage.filters import threshold_otsu
from skimage.filters.rank import median, mean
from skimage.morphology import disk

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

# load two images
dataset1 = gdal.Open('img/mozambique-before-subset.tif')
band1 = dataset1.GetRasterBand(1)
img1 = band1.ReadAsArray().astype(np.uint8)

dataset2 = gdal.Open('img/mozambique-after-subset.tif')
band2 = dataset2.GetRasterBand(1)
img2 = band2.ReadAsArray().astype(np.uint8)

# otsu thresholding of the two images
threshold1 = threshold_otsu(img1)
img_thresholded1 = img1 > threshold1
print 'Threshold for image1:', threshold1

threshold2 = threshold_otsu(img2)
img_thresholded2 = img2 > threshold2
print 'Threshold for image2:', threshold2

# difference between the two thresholded images
img = img_thresholded2 - img_thresholded1
write_image(img, 'img/mozambique-subset-difference-thresholded.tif')
