import glob
import os
import rasterio as rio
import numpy as np
import sys

from time import time


def extract_arrayasdict(raster_root_path, stack_name):

    raster_stack = os.path.join(raster_root_path, stack_name)

    with rio.open(raster_stack) as src:
        profile = src.profile
        bands = [i for i in src.read()]

    keys = ["blue", "green", "red", "NIR", "SWIR1", "SWIR2"]
    dictionary = dict(zip(keys, bands))

    return dictionary, profile


def calculate_NDVI(b_dict):

    red = b_dict["red"]
    nir = b_dict["NIR"]

    red = red.astype(float)
    nir = nir.astype(float)
    print(red.dtype)

    numerator = (red - nir)
    denominator = (red + nir)

    mask = np.equal(denominator, 0)

    denominator[mask] = -99

    ndvi = numerator / denominator

    ndvi[mask] = -99

    index_name = "NDVI"

    return ndvi, index_name

def calculate_NDWI():
    pass

def calculate_TCB():
    pass

def calculate_NDSII():
    pass

def calculate_LWM():
    pass

def calculate_SAVI():
    pass

def save_index_as_GTiff(array, out_path, index_name, profile):

    raster_out = os.path.join(out_path, index_name + ".tif")

    profile.update(dtype=rio.float64, count=1, nodata=-99)

    with rio.open(raster_out,
                  'w',
                  **profile
                  ) as dst:
        dst.write(array, 1)

    print(raster_out)

if __name__ == "__main__":

    # create path to the location of the Landsat GeoTiff files
    raster_path = os.path.join(os.sep,
                               "home",
                               "sebastian",
                               "Documents",
                               "Data",
                               "exemplary_data",
                               "LC819202820160604")
    stack_name = "stack.tif"

    t0 = time()
    dictionary, profile = extract_arrayasdict(raster_path, stack_name)
    print(profile)

    array, index_name = calculate_NDVI(dictionary)
    print(array)
    save_index_as_GTiff(array, raster_path, index_name, profile)



    print("The main function took %.2f seconds." % (time() - t0))