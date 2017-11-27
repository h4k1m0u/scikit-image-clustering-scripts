#!/usr/bin/env python
from sklearn import cluster
from gdal_io import IO


# load dtm image
path_in = '/'.join(('C:', 'Data', 'Tewkesbury-Mask',
                    'SAR_elevation_mask_subset.data', 'band_1_S.img'))
data = IO.read(path_in)
img = data.array

# k-means clustering of the image (population of pixels intensities)
X = img.reshape((-1, 1))
k_means = cluster.KMeans(n_clusters=2)
k_means.fit(X)

# extract means of each cluster & clustered population
clusters_means = k_means.cluster_centers_.squeeze()
X_clustered = k_means.labels_
print('# of Observations:', X.shape)
print('Clusters Means:', clusters_means)

# save clustered image
X_clustered.shape = img.shape
path_out = '/'.join(('C:', 'Data', 'Tewkesbury-Mask', 'kmeans.tif'))
IO.write(X_clustered, path_out, projection=data.projection,
         geocoordinates=data.geocoordinates)
