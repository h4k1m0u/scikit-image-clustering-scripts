#!/usr/bin/env python
# http://stackoverflow.com/questions/9111711/get-coordinates-of-local-maxima-in-2d-array-above-certain-value
import numpy as np
from osgeo import gdal
import scipy.ndimage as ndimage
import scipy.ndimage.filters as filters

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

# position of local maxima
data_max = filters.maximum_filter(img, 5)
maxima = (img == data_max)
data_min = filters.minimum_filter(img, 5)
diff = ((data_max - data_min) > 150)
maxima[diff == 0] = 0

write_image(maxima, 'img/maxima.tif')
