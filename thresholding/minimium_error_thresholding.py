# -*- coding: utf-8 -*-
###############################################################################
# https://gist.github.com/al42and/c2d66f6704e024266108
###############################################################################
import numpy as np
from scipy.misc import imread, imshow


def Kittler(im, out):
    """
    The reimplementation of Kittler-Illingworth Thresholding algorithm:
    https://www.mathworks.com/matlabcentral/fileexchange/45685
    Paper: [Kittler and Illingworth 1986] Minimum error thresholding.

    Works on 8-bit images only.
    """
    h, g = np.histogram(im.ravel(), 256, [0, 256])
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
    out[:, :] = 0
    out[im >= t] = 255


img_in = imread('C:/Github/scikit-image-clustering-scripts/img/Lenna.png',
                True).astype(np.int)
img_out = np.empty_like(img_in)

Kittler(img_in, img_out)
