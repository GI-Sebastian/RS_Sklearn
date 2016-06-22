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

bands = []
for b in raster_list:
    with rio.open(b) as src:
        width = src.width
        height = src.height
        driver = src.driver
        crs = src.crs
        affine = src.affine
        array = src.read(1)
        dtype = array.dtype
        print(array.shape)

        bands.append(array)

ras_out = os.path.join(raster_path,
                       "stack.tif")

with rio.open(ras_out,
              'w',
              width=width,
              height=height,
              driver="GTiff",
              crs=crs,
              affine=affine,
              count=(len(raster_list)+1),
              dtype=dtype
              ) as dst:

    for i, b in enumerate(bands):
        dst.write(b, i+1)