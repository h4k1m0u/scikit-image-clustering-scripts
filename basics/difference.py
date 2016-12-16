#!/usr/bin/env python
import numpy as np
from skimage.filters import threshold_otsu
from geotiff.io import IO


# load two images
DIR = 'C:/Data/Tewkesbury-LiDAR'
img_pre = IO.read(DIR + '/subset.data/Sigma0_HH_slv2_22Jul2008.img')
img_post = IO.read(DIR + '/subset.data/Sigma0_HH_slv1_25Jul2007.img')

# otsu thresholding of the two images
threshold_pre = threshold_otsu(img_pre)
img_thresholded_pre = img_pre < threshold_pre
print 'Threshold for image pre:', threshold_pre
IO.write(img_thresholded_pre, DIR + '/thresholded-pre.tif')

threshold_post = threshold_otsu(img_post)
img_thresholded_post = img_post < threshold_post
print 'Threshold for image post:', threshold_post
IO.write(img_thresholded_post, DIR + '/thresholded-post.tif')

# difference between the two thresholded images
img_difference = np.subtract(img_thresholded_post, img_thresholded_pre,
                             dtype=np.float)
IO.write(img_difference, DIR + '/difference.tif')
