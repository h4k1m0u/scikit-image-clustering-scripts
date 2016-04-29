#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal
from skimage.exposure import histogram

# load original image
dataset = gdal.Open('/home/hakim/Data/Rakhine-Myanmar/during/postimage-subset.data/Sigma0_VV.img')
band = dataset.GetRasterBand(1)
img = band.ReadAsArray().astype(np.float32)

# histogram of the image
hist, bins = histogram(img)
plt.plot(bins, hist)
plt.show()
