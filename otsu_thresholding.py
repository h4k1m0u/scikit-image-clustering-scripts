#!/usr/bin/env python
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.filters import threshold_otsu
from skimage.filters.rank import median, mean
from skimage.morphology import disk

# 1 x 2 grid figure
fig = plt.figure()

# display original image's channel
cell1 = fig.add_subplot(3, 2, 1)
img = io.imread('flood.jpg')[:, :, 0]
io.imshow(img)

# otsu thresholding of the original image
cell2 = fig.add_subplot(3, 2, 2)
threshold = threshold_otsu(img)
thresholded_img = img > threshold
print 'Threshold for original image:', threshold
io.imshow(thresholded_img)

# display original image filtered with a mean filter
cell3 = fig.add_subplot(3, 2, 3)
mean_img = mean(img, disk(11))
io.imshow(mean_img)

# otsu thresholding of the mean-filtered image
cell4 = fig.add_subplot(3, 2, 4)
threshold = threshold_otsu(mean_img)
thresholded_mean_img = mean_img > threshold
print 'Threshold for Mean-filtered image :', threshold
io.imshow(thresholded_mean_img)

# display original image filtered with a median filter
cell5 = fig.add_subplot(3, 2, 5)
median_img = median(img, disk(11))
io.imshow(median_img)

# otsu thresholding of the median-filtered image
cell6 = fig.add_subplot(3, 2, 6)
threshold = threshold_otsu(median_img)
thresholded_median_img = median_img > threshold
print 'Threshold for Median-filtered image:', threshold
io.imshow(thresholded_median_img)

# show figure grid
plt.show()
