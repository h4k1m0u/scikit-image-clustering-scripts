# -*- coding: utf-8 -*-
###############################################################################
# https://gist.github.com/al42and/c2d66f6704e024266108
###############################################################################
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from geotiff.io import IO


def kittler(in_arr):
    """
    The reimplementation of Kittler-Illingworth Thresholding algorithm:
    https://www.mathworks.com/matlabcentral/fileexchange/45685
    Paper: [Kittler and Illingworth 1986] Minimum error thresholding.

    Args:
        in_arr(numpy.ndarray): Input 8-bits array.
    Returns:
        t(int): Calculated threshold.
    """
    h, g = np.histogram(in_arr.ravel(), 256, [0, 256])
    h = h.astype(np.float)
    g = g.astype(np.float)
    g = g[:-1]

    c = np.cumsum(h)
    m = np.cumsum(h * g)
    s = np.cumsum(h * g**2)
    sigma_f = np.sqrt(s/c - (m/c)**2)

    cb = c[-1] - c
    mb = m[-1] - m
    sb = s[-1] - s
    sigma_b = np.sqrt(sb/cb - (mb/cb)**2)

    p = c / c[-1]
    v = p * np.log(sigma_f) + (1-p)*np.log(sigma_b) - p*np.log(p) - \
        (1-p)*np.log(1-p)
    v[~np.isfinite(v)] = np.inf
    idx = np.argmin(v)
    t = g[idx]

    return t


# input image
in_img = Image.open('C:/Github/scikit-image-clustering-scripts/img/Lenna.png')\
              .convert('L')
in_arr = np.asarray(in_img)

#input_file = '/'.join(('C:', 'Data', 'Tewkesbury-SAR',
#                       'building-reconstruction', 'stack.data',
#                       'Sigma0_HH_mst_25Jul2007_db.img'))
#in_arr = IO.read(input_file)

# show input image
plt.figure()
plt.imshow(in_img, cmap='gray')

# output image
t = kittler(in_arr)
out_arr = np.empty_like(in_arr)
out_arr[:, :] = 0
out_arr[in_arr >= t] = 255

# show output image
plt.figure()
plt.imshow(out_arr, cmap='gray')

plt.show()
