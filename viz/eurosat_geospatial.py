import rasterio
from rasterio.plot import show
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import geopandas as gpd
import glob
import os


def show_geospatial_image(file_path):
    img = rasterio.open(file_path)
    image = np.array([img.read(4), img.read(3), img.read(2)]).transpose(1, 2, 0)
    image = image / 4095
    show(image.transpose(2, 0, 1), transform=img.transform)


def show_image(file_path):
    jpg = np.array(Image.open(file_path))
    plt.imshow(jpg)

def plot_world_map(gdf):
    # From GeoPandas, our world map data
    worldmap = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    print(worldmap.crs)

    print(gdf["Latitude"].max(), gdf["Latitude"].min())
    print(gdf["Longitude"].max(), gdf["Longitude"].min())
    #gdf.to_crs(worldmap.crs)
    worldmap.to_crs(gdf.crs)

    fig, ax = plt.subplots(figsize=(12, 6))
    worldmap.plot(color="lightgrey", ax=ax)

    # Plotting our Impact Energy data with a color map
    # x = lon
    # y = lat
    z = 60
    plt.scatter(gdf.Longitude, gdf.Latitude, s=z, c="k", alpha=0.6, vmin=0, cmap='autumn')
    print(gdf.head())
    #gdf.plot(ax=ax, color="red")
    # Creating axis limits and title
    # plt.xlim([-180, 180])
    # plt.ylim([-90, 90])
    plt.title("World map")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()

def get_all_lat_lon(classes=["*"]):
    lat = []
    lon = []
    for c in classes:
        for file in glob.glob(f"data/EuroSATallBands/ds/images/remote_sensing/otherDatasets/sentinel_2/tif/{c}/*"):
            if not os.path.isfile(file):
                continue
            tiff = rasterio.open(file)
            lat.append(tiff.bounds.top  / 100000)
            lon.append(tiff.bounds.left / 100000)
    return (lat, lon)


def create_gdf(lat, lon, crs):

    df = pd.DataFrame(
        {"Latitude": lat,
        "Longitude": lon}
    )
    gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
    gdf = gdf.set_crs(crs)
    return gdf

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
    print(tiff.meta)
    print(tiff.bounds)
    show_geospatial_image(file_path)
    plt.pause(0.5)

    print(tiff.transform)
    x, y = tiff.xy(tiff.height // 2, tiff.width //2)
    print(x,y)
    print(tiff.crs.wkt)

    # #TODO: labels to legend
    # labels = ['AnnualCrop','Forest', 'HerbaceousVegetation', 'Highway',"Industrial", 'Pasture', 'PermanentCrop','Residential', 'River', 'SeaLake']
    
    lat = [tiff.bounds.top  / 100000]
    lon = [tiff.bounds.left / 100000]
    #lat, lon = get_all_lat_lon(["AnnualCrop"])
    crs = tiff.crs
    gdf = create_gdf(lat, lon, crs)
    # TODO: projection error!
    plot_world_map(gdf)


