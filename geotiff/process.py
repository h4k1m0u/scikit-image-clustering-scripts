#!/usr/bin/env python
"""Process images opened with GDAL."""
import logging
from geotiff.io import IO
from sentinel_hub.constants import LOGFILE


# logging to file
logging.basicConfig(
    filename=LOGFILE,
    level=logging.DEBUG,
    format='[LOG] %(asctime)s: %(message)s'
)


class Process:
    """Processing of images opened with GDAL."""

    @staticmethod
    def process(path_in):
        """Open/Process/Write the image in the given path.

        Args:
            path_in(str)
        """
        arr_in = IO.read(path_in)
        arr_out = arr_in
        path_out = path_in
        IO.write(arr_out, path_out)

        logging.info('%s processed [Ok]' % path_in)
