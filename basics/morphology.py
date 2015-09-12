#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal
from skimage.filters import threshold_otsu
from skimage.morphology import binary_dilation, binary_erosion, binary_closing, binary_opening

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
dataset = gdal.Open('../img/mozambique-after.tiff')
band = dataset.GetRasterBand(1)
img = band.ReadAsArray().astype(np.uint8)

# otsu thresholding of the image
threshold = threshold_otsu(img)
img_thresholded = img > threshold
print 'Threshold for original image:', threshold
write_image(img_thresholded, 'img/mozambique-after-thresholded.tiff')

# dilation of the thresholded image
img_thresholded_dilated = binary_dilation(img_thresholded)
write_image(img_thresholded_dilated, 'img/mozambique-after-thresholded-dilated.tiff')

# erosion of the thresholded image
img_thresholded_eroded = binary_erosion(img_thresholded)
write_image(img_thresholded_eroded, 'img/mozambique-after-thresholded-eroded.tiff')

# closing of the thresholded image
img_thresholded_closed = binary_closing(img_thresholded)
write_image(img_thresholded_closed, 'img/mozambique-after-thresholded-closed.tiff')

# opening of the thresholded image
img_thresholded_opened = binary_opening(img_thresholded)
write_image(img_thresholded_opened, 'img/mozambique-after-thresholded-opened.tiff')
