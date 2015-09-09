#!/usr/bin/env python
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.exposure import histogram

# 1 x 2 grid figure
fig = plt.figure()

# display original image as gray scale
cell1 = fig.add_subplot(1, 2, 1)
img = io.imread('flood.jpg', as_grey=True)
plt.imshow(img)

# histogram of the gray scale image
cell2 = fig.add_subplot(1, 2, 2)
hist, bins = histogram(img, 256)
plt.plot(range(256), hist)

# show figure grid
plt.show()
