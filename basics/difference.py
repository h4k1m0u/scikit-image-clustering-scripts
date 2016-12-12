#!/usr/bin/env python
import numpy as np
from osgeo import gdal
from skimage.filters import threshold_otsu


# current directory
DIR = 'C:/Data/Tewkesbury-LiDAR'

# initialize driver
driver = gdal.GetDriverByName('GTiff')


def write_image(img, filename):
    """
    Write img array to a file with the given filename
    Args:
        img (Band)
        filename (str)
    """
    x_size = img.shape[1]
    y_size = img.shape[0]
    dataset = driver.Create(filename, x_size, y_size)
    dataset.GetRasterBand(1).WriteArray(img)


# load two images
dataset_pre = gdal.Open(DIR + '/subset.data/Sigma0_HH_slv2_22Jul2008.img')
band_pre = dataset_pre.GetRasterBand(1)
img_pre = band_pre.ReadAsArray().astype(np.float32)

dataset_post = gdal.Open(DIR + '/subset.data/Sigma0_HH_slv1_25Jul2007.img')
band_post = dataset_post.GetRasterBand(1)
img_post = band_post.ReadAsArray().astype(np.float32)

# otsu thresholding of the two images
threshold_pre = threshold_otsu(img_pre)
img_thresholded_pre = img_pre < threshold_pre
print 'Threshold for image pre:', threshold_pre
write_image(img_thresholded_pre, DIR + '/thresholded-pre.tif')

threshold_post = threshold_otsu(img_post)
img_thresholded_post = img_post < threshold_post
print 'Threshold for image post:', threshold_post
write_image(img_thresholded_post, DIR + '/thresholded-post.tif')

# difference between the two thresholded images
img_difference = img_thresholded_post - img_thresholded_pre
write_image(img_difference, DIR + '/difference.tif')
