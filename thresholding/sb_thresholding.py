#!/usr/bin/env python
"""Split-based thresholding of a GeoTIFF image."""
from skimage.filters import threshold_otsu
from geotiff.io import IO
import numpy as np
from thresholding.kittler_thresholding import min_error_thresholding


# open image
DIR = 'C:/Data/Tewkesbury-LiDAR'
img = IO.read(DIR + '/stack-lidar.data/Sigma0_HH_slv1_25Jul2007.img')

# calculate dB positive image
img_db = 10 * np.log10(img)
img_db[img_db == -np.inf] = np.max(img_db)  # replace 0.0 at the borders
img_db_int = np.round(img_db).astype(int)
img_db_int_pos = img_db_int + abs(np.min(img_db_int))

# constants
img_xsize = img_db_int_pos.shape[0]
img_ysize = img_db_int_pos.shape[1]
SPLIT_SIZE = 100

# extract splits iteratively & their thresholds
sb_otsu_thresholds = []
sb_kittler_thresholds = []
y_offset = 0

while y_offset < img_ysize:
    x_offset = 0
    while x_offset < img_xsize:
        # extract the split
        split_xsize = (
            SPLIT_SIZE if x_offset + SPLIT_SIZE < img_xsize
            else img_xsize - x_offset
        )
        split_ysize = (
            SPLIT_SIZE if y_offset + SPLIT_SIZE < img_ysize
            else img_ysize - y_offset
        )
        split = img_db_int_pos[x_offset:x_offset + split_xsize,
                               y_offset:y_offset + split_ysize]

        # estimate the thereshold of the split
        sb_otsu_thresholds.append(threshold_otsu(split))
        sb_kittler_thresholds.append(min_error_thresholding(
            split,
            np.max(split)
        ))

        x_offset += SPLIT_SIZE

    y_offset += SPLIT_SIZE

# average of local otsu thresholds
sb_otsu_threshold = sum(sb_otsu_thresholds) / len(sb_otsu_thresholds)
print 'SB otsu threshold:', sb_otsu_threshold

# average of local otsu thresholds
sb_kittler_threshold = sum(sb_kittler_thresholds) / len(sb_kittler_thresholds)
print 'SB kittler threshold:', sb_kittler_threshold
