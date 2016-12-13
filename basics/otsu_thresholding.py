#!/usr/bin/env python
from skimage.filters import threshold_otsu
from geotiff.io import IO


# load original image
PATH = 'C:/Data/Tewkesbury-SAR/building-reconstruction'
IN_PATH = PATH + '/stack.data/Sigma0_HH_mst_25Jul2007_db.img'
OUT_PATH = PATH + '/tewkesbury-thresholded.tif'
img = IO.read(IN_PATH)

# otsu thresholding of the original image
threshold = threshold_otsu(img)
img_thresholded = img > threshold
print 'Threshold for original image:', threshold
IO.write(img_thresholded, OUT_PATH)
