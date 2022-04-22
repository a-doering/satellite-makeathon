import rasterio
from rasterio.plot import show
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def show_geospatial_image(file_path):
    img = rasterio.open(file_path)
    image = np.array([img.read(4), img.read(3), img.read(2)]).transpose(1, 2, 0)
    image = image / 4095
    show(image.transpose(2, 0, 1), transform=img.transform)


def show_image(file_path):
    jpg = np.array(Image.open(file_path))
    plt.imshow(jpg)


if __name__ == "__main__":
    i = 1
    # jpg
    file_path = f"data/EuroSAT/2750/AnnualCrop/AnnualCrop_{i}.jpg"
    show_image(file_path)
    plt.pause(0.5)

    # tif
    file_path = f"data/EuroSATallBands/ds/images/remote_sensing/otherDatasets/sentinel_2/tif/AnnualCrop/AnnualCrop_{i}.tif"
    tiff = rasterio.open(file_path)
    print(tiff.bounds)
    show_geospatial_image(file_path)
