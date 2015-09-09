#!/usr/bin/env python
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.filters import threshold_otsu
from skimage.morphology import binary_dilation

# 1 x 2 grid figure
fig = plt.figure()

# display original image's channel
cell1 = fig.add_subplot(1, 3, 1)
img = io.imread('flood.jpg')[:, :, 0]
io.imshow(img)

# otsu thresholding of the image
cell2 = fig.add_subplot(1, 3, 2)
threshold = threshold_otsu(img)
thresholded_img = img > threshold
print 'Threshold:', threshold
io.imshow(thresholded_img)

# dilation of the thresholded image
cell3 = fig.add_subplot(1, 3, 3)
dilated_image = binary_dilation(thresholded_img)
io.imshow(dilated_image)

# show figure grid
plt.show()
