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

# load original image
dataset = gdal.Open('/home/hakim/Data/Rakhine-Myanmar/during/postimage-subset.data/Sigma0_VV.img')
band = dataset.GetRasterBand(1)
img = band.ReadAsArray().astype(np.float32)

# otsu thresholding of the original image
threshold = threshold_otsu(img)
img_thresholded = img > threshold
print 'Threshold for original image:', threshold
write_image(img_thresholded, 'img/rakhine-after-thresholded.tif')
exit()

# image filtered with a mean filter
img_mean = mean(img, disk(1))

# otsu thresholding of the mean-filtered image
threshold = threshold_otsu(img_mean)
img_mean_thresholded = img_mean > threshold
print 'Threshold for Mean-filtered image :', threshold
write_image(img_mean_thresholded, 'img/mozambique-after-mean-thresholded.tif')

# image filtered with a median filter
img_median = median(img, disk(1))

# otsu thresholding of the median-filtered image
threshold = threshold_otsu(img_median)
img_median_thresholded = img_median > threshold
print 'Threshold for Median-filtered image:', threshold
write_image(img_median_thresholded, 'img/mozambique-after-median-thresholded.tif')
