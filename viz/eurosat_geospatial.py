import rasterio
from rasterio.plot import show
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import geopandas as gpd


def show_geospatial_image(file_path):
    img = rasterio.open(file_path)
    image = np.array([img.read(4), img.read(3), img.read(2)]).transpose(1, 2, 0)
    image = image / 4095
    show(image.transpose(2, 0, 1), transform=img.transform)


def show_image(file_path):
    jpg = np.array(Image.open(file_path))
    plt.imshow(jpg)

def plot_world_map(lat, lon, labels):
    # From GeoPandas, our world map data
    worldmap = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

    fig, ax = plt.subplots(figsize=(12, 6))
    worldmap.plot(color="lightgrey", ax=ax)

    # Plotting our Impact Energy data with a color map
    x = lon
    y = lat
    z = 60
    plt.scatter(x, y, s=z, c="k", alpha=0.6, vmin=0, cmap='autumn')

    # Creating axis limits and title
    plt.xlim([-180, 180])
    plt.ylim([-90, 90])
    plt.title("World map")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()

if __name__ == "__main__":
    i = 1500
    # jpg
    file_path = f"data/EuroSAT/2750/AnnualCrop/AnnualCrop_{i}.jpg"
    show_image(file_path)
    plt.pause(0.5)

    # tif
    file_path = f"data/EuroSATallBands/ds/images/remote_sensing/otherDatasets/sentinel_2/tif/AnnualCrop/AnnualCrop_{i}.tif"
    tiff = rasterio.open(file_path)
    print(tiff.bounds)
    show_geospatial_image(file_path)
    plt.pause(0.5)

    #TODO: fix crs system and add labels to legend
    print(tiff.crs)
    labels = ['AnnualCrop','Forest', 'HerbaceousVegetation', 'Highway',"Industrial", 'Pasture', 'PermanentCrop','Residential', 'River', 'SeaLake']
    plot_world_map([tiff.bounds.top / 100000],[tiff.bounds.left / 100000],  labels)



