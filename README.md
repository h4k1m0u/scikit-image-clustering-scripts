# Scikit Image Clustering Scripts:
`Python` scripts using `scikit-image` and `scikit-learn` to cluster images.

## files:
**basics/otsu_thresholding.py**: Performs the Otsu thresholding and show the original gray-scale image and the binarized image.  
**basics/histogram.py**: Calculates & show the histogram of the gray scale image.  
**basics/morphology.py**: Dilates/Erodes/Closes/Opens the binary thresholded image.  
**basics/equalization.py**: Thresholding a histogram-equalized image (enhanced in contrast).  
**basics/difference.py**: performs arithmetic difference between two images.
**preprocessing/adaptive_filters.py**: Compare adaptive filters (lee, frost, kuan) to mean/median filters.
**clustering/kmeans_clustering.py**: Performs a k-means clustering followed by an Otsu thresholding.
**clustering/gaussian_mixture_model.py**: Gaussian Mixture Model on image population.
**clustering/lbp_texture.py**: Local Binary Pattern texture segmentation.
**clustering/mean_shift.py**: Performs the Mean Shift algorithm on the image.
**segmentation/flood_fill.py**: 8-neighbours flood fill with prior initialization.
**segmentation/fill_holes.py**: Fill both black and white holes.
**segmentation/local_maxima.py**: Detect objects using local maxima.

## Prerequisites:
**numpy & scipy**: `pip install numpy scipy`  
**scikit-image**: `pip install scikit-image`  
**scikit-learn**: `pip install scikit-learn`  
**pyradar**: `pip install pyradar`  
**gdal-gdal**: `apt-get install python-gdal`
