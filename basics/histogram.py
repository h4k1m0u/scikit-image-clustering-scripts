#!/usr/bin/env python
import matplotlib.pyplot as plt
from geotiff.io import IO


# load original image
input_file = '/'.join(('C:', 'Data', 'Tewkesbury-LiDAR', 'subset.data',
                       'Sigma0_HH_slv1_25Jul2007.img'))
img = IO.read(input_file)

# histogram of the image
plt.hist(img.flatten(), bins=10, range=[0, 10])
plt.show()
