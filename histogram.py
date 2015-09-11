#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal
from skimage.exposure import histogram

# display original image's channel 
dataset = gdal.Open('img/mozambique-after.tiff')
band = dataset.GetRasterBand(1)
img = band.ReadAsArray().astype(np.uint8)

# histogram of the gray scale image
hist, bins = histogram(img)
plt.plot(bins, hist)
plt.show()
