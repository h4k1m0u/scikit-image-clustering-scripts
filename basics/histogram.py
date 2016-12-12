#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal
from skimage.exposure import histogram


# load original image
input_file = '/'.join(('C:', 'Data', 'Tewkesbury-LiDAR', 'stack-lidar.data',
                       'Sigma0_HH_slv1_25Jul2007.img'))
dataset = gdal.Open(input_file)
band = dataset.GetRasterBand(1)
img = band.ReadAsArray().astype(np.float32)

# histogram of the image
hist, bins = histogram(img, nbins=10)
plt.plot(bins, hist)
plt.show()
