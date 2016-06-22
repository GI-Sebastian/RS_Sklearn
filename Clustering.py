import glob
import numpy as np
import os
import rasterio as rio
from sklearn import decomposition

# create path to the location of the Landsat GeoTiff files
raster_path = os.path.join(os.sep,
                           "home",
                           "sebastian",
                           "Documents",
                           "Data",
                           "exemplary_data",
                           "LC819202820160604")

# iterate over all files matching this Unix style pattern
raster_list = []
for name in glob.glob(raster_path + "/*B[2-7].TIF"):
    raster_list.append(name)

# sort the list
raster_list = sorted(raster_list)

band_list = []
for raster in raster_list:
    with rio.open(raster) as src:
        array = src.read()
        band_list.append(array)

pixels = np.dstack([c.ravel() for c in band_list])[0]

pca = decomposition.PCA(n_components=6, whiten=False)
pca.fit(pixels)

for band in range(len(pca.components_)):
    print(
    'Band %s explains %s of variance. Weights:'
    % (band+1, pca.explained_variance_ratio_[band])
    )
    print(np.around(pca.components_[band], decimals=2))