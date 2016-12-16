# -*- coding: utf-8 -*-
###############################################################################
# https://github.com/fiji/Auto_Threshold/
###############################################################################
import numpy as np
from math import isnan, floor
from geotiff.io import IO


def A(y, j):
    """
        Args:
            y(numpy.ndarray): Histogram.
            j(int): Last index in the sum.

        Returns:
            a(float)
    """
    a = sum(y[0:j+1])

    return float(a)


def B(y, j):
    """
        Args:
            y(numpy.ndarray): Histogram.
            j(int) Last index in the sum.

        Returns:
            b(float)
    """
    ind = np.arange(0, j+1)
    b = np.dot(ind, y[0:j+1].T)

    return float(b)


def C(y, j):
    """
        Args:
            y(numpy.ndarray): Histogram.
            j(int) Last index in the sum.

        Returns:
            c(float)
    """
    ind = np.arange(0, j+1)
    c = np.dot(ind**2, y[0:j+1].T)

    return float(c)


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


def min_error_thresholding(arr, n):
    """
        Args:
            arr(numpy.ndarray): 1D image vector.
            n(int): Number of histogram bins.

        Returns:
            t(int): Mean-error threshold of the histogram.
    """
    t = int(round(np.mean(arr)))
    t_prev = np.nan

    # image histogram
    h = np.bincount(arr.ravel(), minlength=n+1)

    while t != t_prev:
        # calculate some statistics
        mu = B(h, t) / A(h, t)
        nu = (B(h, n) - B(h, t)) / (A(h, n) - A(h, t))
        p = A(h, t) / A(h, n)
        q = (A(h, n) - A(h, t)) / A(h, n)
        sigma2 = C(h, t) / A(h, t) - mu**2
        tau2 = (C(h, n) - C(h, t)) / (A(h, n) - A(h, t)) - nu**2

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
        temp = (w1 + np.sqrt(sqterm)) / w0

        if isnan(temp):
            print "MinError(I): not converging. (2)"
            t = t_prev
        else:
            t = int(floor(temp))

    return t


# open image, convert to dB, and shift to positive values
DIR = 'C:/Data/Tewkesbury-LiDAR'
img = IO.read(DIR + '/subset.data/Sigma0_HH_slv1_25Jul2007.img')
img_db = 10 * np.log10(img)
img_db_int = np.round(img_db).astype(int)
img_db_int_pos = img_db_int + abs(np.min(img_db_int))

# calculate threshold
n = np.max(img_db_int_pos)  # 255
threshold = min_error_thresholding(img_db_int_pos.ravel(), n)
print 'threshold:', threshold
