import numpy as np
import numpy.testing as npt
import unittest

from remote_sensing_utilities import indices


class Test(unittest.TestCase):

    def test_calculateNDVI_returns_correct_results_1(self):

        keys = ["blue", "green", "red", "NIR", "SWIR1", "SWIR2"]
        bands = [np.ones(shape=(2, 2)) for b in keys]
        band_dictionary = dict(zip(keys, bands))
        test_1 = indices.RasterBand(band_dictionary)
        test_ndvi = test_1.calculateNDVI()
        correct_result = np.zeros(shape=(2, 2))
        false_result = np.ones(shape=(2, 2)) * 2

        npt.assert_array_equal(test_ndvi, correct_result)
        npt.assert_array_equal(test_ndvi, correct_result)

    def test_calculateNDVI_returns_correct_results_2(self):

        keys = ["blue", "green", "red", "NIR", "SWIR1", "SWIR2"]
        bands = []
        for key in keys:
            if key == "red":
                band = np.array([[1, 2], [3, 4]])
            elif key == "NIR":
                band = np.array([[4, 3], [2, 1]])
            else:
                band = np.zeros(shape=(2, 2))
            bands.append(band)
        band_dictionary = dict(zip(keys, bands))
        test = indices.RasterBand(band_dictionary)
        test_ndvi = test.calculateNDVI()
        correct_result = np.array([[0.6, 0.2], [-0.2, -0.6]])

    def test_calculateNDWI_returns_correct_results_1(self):

        keys = ["blue", "green", "red", "NIR", "SWIR1", "SWIR2"]
        bands = [np.ones(shape=(2, 2)) for b in keys]
        band_dictionary = dict(zip(keys, bands))
        test_1 = indices.RasterBand(band_dictionary)
        test_ndvi = test_1.calculateNDWI()
        correct_result = np.zeros(shape=(2, 2))
        false_result = np.ones(shape=(2, 2)) * 2

        npt.assert_array_equal(test_ndvi, correct_result)
        npt.assert_array_equal(test_ndvi, correct_result)

    def test_calculateNDWI_returns_correct_results_2(self):

        keys = ["blue", "green", "red", "NIR", "SWIR1", "SWIR2"]
        bands = []
        for key in keys:
            if key == "SWIR1":
                band = np.array([[1, 2], [3, 4]])
            elif key == "NIR":
                band = np.array([[4, 3], [2, 1]])
            else:
                band = np.zeros(shape=(2, 2))
            bands.append(band)
        band_dictionary = dict(zip(keys, bands))
        test = indices.RasterBand(band_dictionary)
        test_ndvi = test.calculateNDWI()
        correct_result = np.array([[0.6, 0.2], [-0.2, -0.6]])

        npt.assert_array_equal(test_ndvi, correct_result)
        npt.assert_array_equal(test_ndvi, correct_result)

        npt.assert_array_equal(test_ndvi, correct_result)
        npt.assert_array_equal(test_ndvi, correct_result)


if __name__ == '__main__':



    unittest.main()

