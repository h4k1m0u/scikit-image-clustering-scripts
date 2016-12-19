#!/usr/bin/env python
from skimage.filters import threshold_otsu
from geotiff.io import IO
import numpy as np


# open image
DIR = 'C:/Data/Tewkesbury-LiDAR'
img = IO.read(DIR + '/stack-lidar.data/Sigma0_HH_slv1_25Jul2007.img')

# calculate dB positive image
img_db = 10 * np.log10(img)
img_db[img_db == -np.inf] = np.max(img_db)  # remove 0.0 values at the borders
img_db_int = np.round(img_db).astype(int)
img_db_int_pos = img_db_int + abs(np.min(img_db_int))

# otsu thresholding
threshold = threshold_otsu(img_db_int_pos)
print 'Otsu threshold:', threshold
