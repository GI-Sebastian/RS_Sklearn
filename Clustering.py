import glob
import os
import rasterio as rio

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

print band_list
