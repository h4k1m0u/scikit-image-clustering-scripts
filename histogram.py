#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal
from skimage.exposure import histogram

# load original image
dataset = gdal.Open('img/mozambique-after.tiff')
band = dataset.GetRasterBand(1)
img = band.ReadAsArray().astype(np.uint8)

# histogram of the image
hist, bins = histogram(img)
plt.plot(bins, hist)
plt.show()
