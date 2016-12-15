# -*- coding: utf-8 -*-
###############################################################################
# https://github.com/fiji/Auto_Threshold/
###############################################################################
from PIL import Image
import numpy as np
from math import log10, sqrt, isnan, floor
import matplotlib.pyplot as plt


def A(y, j):
    """
        Args:
            y(numpy.ndarray): Histogram.
            j(int): Last index in the sum.

        Returns:
            x(float)
    """
    return sum(y[1:j+2])


def B(y, j):
    """
        Args:
            y(numpy.ndarray): Histogram.
            j(int) Last index in the sum.

        Returns:
            x(float)
    """
    ind = np.arange(0, j+1)

    return np.dot(ind, y[1:j+2].T)


def C(y, j):
    """
        Args:
            y(numpy.ndarray): Histogram.
            j(int) Last index in the sum.

        Returns:
            x(float)
    """
    ind = np.arange(0, j+1)

    return np.dot(ind**2, y[1:j+2].T)


def mean(h):
    """
        Args:
            h(numpy.ndarray): Image histogram.

        Returns:
            t(int): Mean threshold of the histogram.
    """
    t = -1
    tot = 0
    sum = 0

    for i in xrange(h.shape[0]):
        tot += h[i]
        sum += (i * h[i])

    t = int(floor(sum / tot))

    return t


def min_error_thresholding(arr):
    """
        Args:
            arr(numpy.ndarray): 1D image vector.

        Returns:
            t(int): Mean-error threshold of the histogram.
    """
    n = 256
    t = round(np.mean(arr))
    t_prev = np.nan

    # image histogram
    h, g = np.histogram(arr, 256, [0, 256])

    while t != t_prev:
        print 't', t

        # calculate some statistics
        mu = B(h, t) / A(h, t)
        nu = (B(h, n) - B(h, t)) / \
             (A(h, n) - A(h, t))
        p = A(h, t) / A(h, n)
        q = (A(h, n) - A(h, t)) / A(h, n)
        sigma2 = C(h, t) / A(h, t) - mu**2
        tau2 = (C(h, n) - C(h, t)) / \
               (A(h, n) - A(h, t)) - nu**2

        # the terms of the quadratic equation to be solved
        w0 = 1.0/sigma2 - 1.0/tau2
        w1 = mu/sigma2 - nu/tau2
        w2 = mu**2/sigma2 - nu**2/tau2 + \
            np.log10((sigma2 * q**2) / (tau2 * p**2))

        # if the next threshold would be imaginary, return with the current one
        sqterm = w1**2 - w0*w2

        if sqterm < 0:
            print "MinError(I): not converging. (1)"
            return t

        # The updated threshold is the integer part of the solution of the
        # quadratic equation
        t_prev = t
        temp = (w1 + sqrt(sqterm)) / w0

        if isnan(temp):
            print "MinError(I): not converging. (2)"
            t = t_prev
        else:
            t = int(floor(temp))

    return t


# input image & its histogram
img_in = Image.open(
    'C:/Github/scikit-image-clustering-scripts/img/Lenna.png'
).convert('L')
arr_in = np.asarray(img_in)

# A, B, C
h, g = np.histogram(arr_in.ravel(), 256, [0, 256])
print 'A: %f' % A(h, 124)
print 'B: %f' % B(h, 124)
print 'C: %f' % C(h, 124)

# plot estimation
# plt.hist(arr_in, 256)
# plt.show()

# threshold = min_error_thresholding(arr_in.ravel())
