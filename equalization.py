#!/usr/bin/env python
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.filters import threshold_otsu
from skimage.exposure import equalize_hist

# 1 x 2 grid figure
fig = plt.figure()

# display original image's channel
cell1 = fig.add_subplot(1, 3, 1)
img = io.imread('flood.jpg')[:, :, 0]
io.imshow(img)

# histogram-equalization of the image (enhance contrast)
cell2 = fig.add_subplot(1, 3, 2)
contrasted_img = equalize_hist(img)
io.imshow(contrasted_img)

# otsu thresholding of the image
cell3 = fig.add_subplot(1, 3, 3)
threshold = threshold_otsu(contrasted_img)
thresholded_img = contrasted_img > threshold
print 'Threshold:', 255 * threshold
io.imshow(thresholded_img)

# show figure grid
plt.show()
