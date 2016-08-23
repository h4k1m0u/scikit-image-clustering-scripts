#!/usr/bin/env python
"""Split-based thresholding of a GeoTIFF image."""
from skimage.filters import threshold_otsu
from geotiff.io import IO


# constants
SPLIT_SIZE = 100
PATH = 'C:/Data'
IN_PATH = PATH + '/namibia-flipped.data/Sigma0_HH.img'
OUT_PATH = PATH + '/namibia-splits/serbia-split-(%s,%s).tiff'

# load original image
img = IO.read(IN_PATH)
img_xsize = img.shape[1]
img_ysize = img.shape[0]

# extract splits iteratively & their thresholds
local_thresholds = []
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
        local_thresholds.append(threshold_otsu(split))

        x_offset += SPLIT_SIZE

    y_offset += SPLIT_SIZE

# average of local otsu thresholds
local_threshold = sum(local_thresholds) / len(local_thresholds)
print 'Local threshold:', local_threshold

# global otsu threshold
global_threshold = threshold_otsu(img)
print 'Global threshold:', global_threshold

# otsu thresholding using the average of splits thresholds
img_thresholded = img > local_threshold
IO.write(img_thresholded, 'C:/Data/namibia-flipped-split-thresholded.tif')
