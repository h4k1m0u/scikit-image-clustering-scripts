# -*- coding: utf-8 -*-
###############################################################################
# https://github.com/fiji/Auto_Threshold/
###############################################################################
from PIL import Image
import numpy as np
from math import log10, sqrt, isnan, floor


def A(y, j):
    """
        Args:
            y(numpy.ndarray)
            j(int)

        Returns:
            x(int)
    """
    x = 0
    for i in xrange(j + 1):
        x += y[i]

    return x


def B(y, j):
    """
        Args:
            y(numpy.ndarray)
            j(int)

        Returns:
            x(int)
    """
    x = 0
    for i in xrange(j + 1):
        x += i * y[i]

    return x


def C(y, j):
    """
        Args:
            y(numpy.ndarray)
            j(int)

        Returns:
            x(int)
    """
    x = 0
    for i in xrange(j + 1):
        x += i * i * y[i]

    return x


def min_error_thresholding(h):
    t = np.mean(h)
    t_prev = -2

    while t != t_prev:
        # calculate some statistics
        mu = B(h, t) / A(h, t)
        nu = (B(h, h.shape[0] - 1) - B(h, t)) / \
             (A(h, h.shape[0] - 1) - A(h, t))
        p = A(h, t) / A(h, h.shape[0] - 1)
        q = (A(h, h.shape[0] - 1) - A(h, t)) / A(h, h.shape[0] - 1)
        sigma2 = C(h, t) / A(h, t) - mu**2
        tau2 = (C(h, h.shape[0] - 1) - C(h, t)) / \
               (A(h, h.shape[0] - 1) - A(h, t)) - nu**2

        # the terms of the quadratic equation to be solved
        w0 = 1.0/sigma2 - 1.0/tau2
        w1 = mu/sigma2 - nu/tau2
        w2 = mu**2/sigma2 - nu**2/tau2 + log10((sigma2 * q**2) / (tau2 * p**2))

        # if the next threshold would be imaginary, return with the current one
        sqterm = w1**2 - w0*w2
        if sqterm < 0:
            print "MinError(I): not converging."
            return t

        # The updated threshold is the integer part of the solution of the
        # quadratic equation
        t_prev = t
        temp = (w1 + sqrt(sqterm)) / w0
        if isnan(temp):
            print "MinError(I): not converging."
            t = t_prev
        else:
            t = int(floor(temp))

    return t


# input image & its histogram
img_in = Image.open('C:/Github/scikit-image-clustering-scripts/img/Lenna.png')\
           .convert('L')
arr_in = np.asarray(img_in)
h, g = np.histogram(arr_in.ravel(), 256, [0, 256])
threshold = min_error_thresholding(h)
