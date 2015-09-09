#!/usr/bin/env python
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.exposure import histogram, cumulative_distribution

# 1 x 2 grid figure
fig = plt.figure()

# display original image's channel 
cell1 = fig.add_subplot(1, 3, 1)
img = io.imread('flood.jpg')[:, :, 0]
io.imshow(img)

# histogram of the gray scale image
cell2 = fig.add_subplot(1, 3, 2)
hist, bins = histogram(img)
plt.plot(bins, hist)

# accumulated histogram of the gray scale image
cell3 = fig.add_subplot(1, 3, 3)
hist, bins = cumulative_distribution(img)
plt.plot(bins, hist)

# show figure grid
plt.show()
