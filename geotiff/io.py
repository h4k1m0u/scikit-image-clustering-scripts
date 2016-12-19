#!/usr/bin/env python
"""Read/Write operations on images opened with GDAL."""
from osgeo import gdal


class IO:
    """IO operations on images opened with GDAL."""

    @staticmethod
    def read(filename):
        """
        Read image with the given filename as an array.

        Args:
            filename (str)
        Returns:
            img (numpy.ndarray)
        """
        # load original image
        dataset = gdal.Open(filename)
        band = dataset.GetRasterBand(1)
        arr = band.ReadAsArray()
        return arr

    @staticmethod
    def write(arr, filename):
        """
        Write image array to a file with the given filename.

        Args:
            arr (numpy.ndarray)
            filename (str)
        """
        driver = gdal.GetDriverByName('GTiff')
        x_size = arr.shape[1]
        y_size = arr.shape[0]
        dataset = driver.Create(filename, x_size, y_size,
                                eType=gdal.GDT_Float32)
        dataset.GetRasterBand(1).WriteArray(arr)
