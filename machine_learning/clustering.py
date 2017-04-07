import os
import rasterio as rio

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

    raster = os.path.join(raster_path, stack_name)

    with rio.open(raster) as src:
        pass
