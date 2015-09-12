#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal
from skimage.filters import threshold_otsu
from skimage.filters.rank import median, mean
from skimage.morphology import disk
from pyradar.filters.lee import lee_filter
from pyradar.filters.frost import frost_filter
from pyradar.filters.kuan import kuan_filter

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
img = band.ReadAsArray()

# lee filter
img_lee = lee_filter(img, win_size=3)
write_image(img_lee.astype(np.uint8), '../img/mozambique-after-subset-lee.tiff')

# frost filter
img_frost = frost_filter(img, win_size=3)
write_image(img_frost.astype(np.uint8), '../img/mozambique-after-subset-frost.tiff')

# kuan filter
img_kuan = kuan_filter(img, win_size=3)
write_image(img_kuan.astype(np.uint8), '../img/mozambique-after-subset-kuan.tiff')
