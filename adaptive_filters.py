#!/usr/bin/env python
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.filters import threshold_otsu
from skimage.filters.rank import median, mean
from skimage.morphology import disk
from pyradar.filters.lee import lee_filter
from pyradar.filters.frost import frost_filter
from pyradar.filters.kuan import kuan_filter

# 3 x 2 grid figure
fig = plt.figure()

# display original image's channel
cell1 = fig.add_subplot(3, 2, 1)
img = io.imread('flood.jpg')[:, :, 0]
io.imshow(img)

# mean filter
cell2 = fig.add_subplot(3, 2, 2)
mean_img = mean(img, disk(1))
io.imshow(mean_img)

# median filter
cell3 = fig.add_subplot(3, 2, 3)
median_img = median(img, disk(1))
io.imshow(median_img)

# lee filter
cell4 = fig.add_subplot(3, 2, 4)
lee_img = lee_filter(img, win_size=3)
io.imshow(lee_img)

# frost filter
cell5 = fig.add_subplot(3, 2, 5)
frost_img = frost_filter(img, win_size=3)
io.imshow(frost_img)

# kuan filter
cell6 = fig.add_subplot(3, 2, 6)
kuan_img = kuan_filter(img, win_size=3)
io.imshow(kuan_img)

# show figure grid
plt.show()
plt.savefig('figure.png')
