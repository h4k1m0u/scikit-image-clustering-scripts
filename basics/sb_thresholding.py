#!/usr/bin/env python
"""Split-based thresholding of a GeoTIFF image."""
from skimage.filters import threshold_otsu
from geotiff.io import IO


# constants
SPLIT_SIZE = 100
PATH = 'C:/Data/Tewkesbury-SAR/building-reconstruction'
IN_PATH = PATH + '/stack.data/Sigma0_HH_mst_25Jul2007_db.img'

# load original image
img = IO.read(IN_PATH)
img_xsize = img.shape[1]
img_ysize = img.shape[0]

# extract splits iteratively & their thresholds
splits_thresholds = []
y_offset = 0
while y_offset < img_ysize:
    x_offset = 0
    while x_offset < img_xsize:
        # estimate the otsu threshold for each split
        split_xsize = (
            SPLIT_SIZE if x_offset + SPLIT_SIZE < img_xsize
            else img_xsize - x_offset
        )
        split_ysize = (
            SPLIT_SIZE if y_offset + SPLIT_SIZE < img_ysize
            else img_ysize - y_offset
        )
        split = img[x_offset:x_offset + split_xsize,
                    y_offset:y_offset + split_ysize]
        splits_thresholds.append(threshold_otsu(split))

        x_offset += SPLIT_SIZE

    y_offset += SPLIT_SIZE

# global otsu threshold
global_threshold = threshold_otsu(img)
print 'Global threshold: %f dB' % global_threshold

# average of local otsu thresholds
avg_split_threshold = sum(splits_thresholds) / len(splits_thresholds)
print 'Split threshold: %f dB' % avg_split_threshold

# otsu thresholding
img_thresholded = img > global_threshold
IO.write(img_thresholded, PATH + '/tewkesbury-thresholded.tif')

# split-based thresholding
img_sb_thresholded = img > avg_split_threshold
IO.write(img_sb_thresholded, PATH + '/tewkesbury-sb-thresholded.tif')
