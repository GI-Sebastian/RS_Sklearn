import glob
import os
import rasterio as rio
import numpy as np
import sys

from time import time


# NOTE: maybe I should create a class for raster IO used in these scripts
def extractArrayAsDict(raster_root_path, stack_name):

    raster_stack = os.path.join(raster_root_path, stack_name)

    with rio.open(raster_stack) as src:
        profile = src.profile
        bands = [i for i in src.read()]

    keys = ["blue", "green", "red", "NIR", "SWIR1", "SWIR2"]
    band_dictionary = dict(zip(keys, bands))

    return band_dictionary, profile


def saveIndexAsGtiff(array, out_path,  profile):

    with rio.open(out_path,
                  'w',
                  **profile
                  ) as dst:
        dst.write(array, 1)


class RasterBand(object):

    no_data = -9999

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.blue = self.dictionary["blue"]
        self.green = self.dictionary["green"]
        self.red = self.dictionary["red"]
        self.nir = self.dictionary["NIR"]
        self.swir1 = self.dictionary["SWIR1"]
        self.swir2 = self.dictionary["SWIR2"]

    def calculateNDVI(self):
        numerator = (self.red + self.nir)
        denominator = (self.red - self.nir)

        mask = np.equal(denominator, 0)
        denominator[mask] = self.no_data

        ndvi = numerator / denominator

        ndvi[mask] = self.no_data

        return ndvi

    def ndwi(self):
        pass

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
    dictionary, profile = extractArrayAsDict(raster_path, stack_name)

    rb = RasterBand(dictionary)
    ndvi = rb.calculateNDVI()

    profile.update(dtype=rio.float64, count=1, nodata=rb.no_data)

    ras_out = os.path.join(raster_path, "NDVI.tif")

    saveIndexAsGtiff(array=ndvi,
                     out_path=ras_out,
                     profile=profile)


    print("The main function took %.2f seconds." % (time() - t0))