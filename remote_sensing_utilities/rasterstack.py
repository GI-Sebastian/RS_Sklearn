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

# iterate over all raster files in the raster_list, read the GTiff as an
# array, and append them to the bands list object
# Additionally, all properties from the raster files are stored in variables
# these properties are needed for the creation of a new GTiff
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

# define the output GTiff file
ras_out = os.path.join(raster_path,
                       "stack.tif")

# create the new GTiff raster, where all array objects will be stored as
# separated raster bands
with rio.open(ras_out,
              'w',
              width=width,
              height=height,
              driver="GTiff",
              crs=crs,
              affine=affine,
              count=(len(bands)+1),   # the count indicates the number
              # of raster bands in this GTiff file. This number is not
              # 0-indexed and therefor the length of the bands list must be
              # altered by +1
              dtype=dtype
              ) as dst:
    # iterate over the bands list and write them as band to the GTiff file
    for i, b in enumerate(bands):
        dst.write(b, i+1)
        
