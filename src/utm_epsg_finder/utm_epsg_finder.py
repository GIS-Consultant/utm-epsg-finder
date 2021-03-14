"""Main module."""
import geopandas
import rasterio
import utm
from pyproj import CRS
from shapely.geometry import Polygon


def line_find_utm_epsg(input_data_path: str) -> str:
    """Find EPSG code of the line's centroid.

    If line's EPSG is 4326 or 3857 it will reprojected
    into its relative UTM EPSG.

    Args:
        input_data_path: String path.

    Returns:
        String.
    """
    if type(input_data_path) is not geopandas.geodataframe.GeoDataFrame:
        input_vector = geopandas.read_file(input_data_path)
    else:
        input_vector = input_data_path

    # Check if vector_in's EPSG is 4326 or 3857
    if input_vector.crs == "epsg:4326" or input_vector.crs == "epsg:3857":

        if input_vector.crs != "epsg:4326":
            # Reproject vector_in from 3857 to 4326
            vector_in_to_4326 = input_vector.to_crs(4326)
            input_vector = vector_in_to_4326

        # Extract centroid coordinates
        lon = input_vector.centroid[0].x
        lat = input_vector.centroid[0].y

        # Check EPSG
        crs = CRS.from_dict(
            {
                "proj": "utm",
                "zone": utm.from_latlon(lat, lon)[2],
            }
        ).to_authority()[1]

        epsg = "epsg:" + crs
        return epsg
    else:
        epsg = input_vector.crs
        return epsg


def point_find_utm_epsg(input_data_path: str) -> str:
    """Find EPSG code of the point.

    If point's EPSG is 4326 or 3857 it will reprojected
    into its relative UTM EPSG.

    Args:
        input_data_path: String path.

    Returns:
        String.
    """
    if type(input_data_path) is not geopandas.geodataframe.GeoDataFrame:
        input_vector = geopandas.read_file(input_data_path)
    else:
        input_vector = input_data_path

    # Check if vector_in's EPSG is 4326 or 3857
    if input_vector.crs == "epsg:4326" or input_vector.crs == "epsg:3857":

        if input_vector.crs != "epsg:4326":
            # Reproject vector_in from 3857 to 4326
            vector_in_to_4326 = input_vector.to_crs(4326)
            input_vector = vector_in_to_4326

        # Extract longitude and latitude
        lon = input_vector["geometry"].x[0]
        lat = input_vector["geometry"].y[0]

        # Check EPSG
        crs = CRS.from_dict(
            {
                "proj": "utm",
                "zone": utm.from_latlon(lat, lon)[2],
            }
        ).to_authority()[1]

        epsg = "epsg:" + crs
        return epsg

    else:
        epsg = input_vector.crs
        return epsg


def polygon_find_utm_epsg(input_data_path: str) -> str:
    """Find EPSG code of the polygon's centroid.

    If polygon's EPSG is 4326 or 3857 it will reprojected
    into its relative UTM EPSG.

    Args:
        input_data_path: String path.

    Returns:
        String.
    """
    if type(input_data_path) is not geopandas.geodataframe.GeoDataFrame:
        input_vector = geopandas.read_file(input_data_path)
    else:
        input_vector = input_data_path

    # Check if vector_in's EPSG is 4326 or 3857
    if input_vector.crs == "epsg:4326" or input_vector.crs == "epsg:3857":

        if input_vector.crs != "epsg:4326":
            # Reproject vector_in from 3857 to 4326
            vector_in_to_4326 = input_vector.to_crs(4326)
            input_vector = vector_in_to_4326

        # Extract centroid coordinates
        lon = input_vector.centroid[0].x
        lat = input_vector.centroid[0].y

        # Check EPSG
        crs = CRS.from_dict(
            {
                "proj": "utm",
                "zone": utm.from_latlon(lat, lon)[2],
            }
        ).to_authority()[1]

        epsg = "epsg:" + crs
        return epsg

    else:
        epsg = input_vector.crs
        return epsg


def raster_find_utm_epsg(input_data_path: str) -> str:
    """Find EPSG code of the raster's centroid.

    If raster's EPSG is 4326 or 3857 it will reprojected
    into its relative UTM EPSG.

    Args:
        input_data_path: String path.

    Returns:
        String.
    """
    if type(input_data_path) is not rasterio.io.DatasetReader:
        raster_in = rasterio.open(input_data_path)
    else:
        raster_in = input_data_path

    # Get raster boundary box coordinates
    bbox = raster_in.bounds

    # Create coordinate arrays
    lat_list = [bbox.bottom, bbox.top, bbox.bottom]
    lon_list = [bbox.left, bbox.right, bbox.left]

    # Create polygon and covert it into GeoDataFrame
    polygon_bbox = Polygon(zip(lon_list, lat_list))
    gdf = geopandas.GeoDataFrame(geometry=[polygon_bbox], crs=raster_in.crs)

    # Get EPSG
    epsg = polygon_find_utm_epsg(gdf)
    return epsg
