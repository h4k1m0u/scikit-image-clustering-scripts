#!/usr/bin/env python
from skimage.filters import threshold_otsu
from geotiff.io import IO


# load original image
img = IO.read('C:/Data/namibia-flipped.data/Sigma0_HH.img')

# otsu thresholding of the original image
threshold = threshold_otsu(img)
img_thresholded = img > threshold
print 'Threshold for original image:', threshold
IO.write(img_thresholded, 'C:/Data/namibia-flipped-thresholded.tif')
