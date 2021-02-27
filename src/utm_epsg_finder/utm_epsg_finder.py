"""Main module."""
import geopandas as gpd
import utm
from pyproj import CRS


def polygon_find_utm_epsg(vector_path: str) -> str:
    """Find EPSG code of the polygon's centroids.

    If polygon's EPSG is 4326 or 3857 it will reprojected
    into its relative UTM EPSG. Since with Pseudo-Mercator
    is not optimal calculate area, you choose to
    reproject polygon in its UTM EPSG.

    Args:
        vector_path: String path.

    Returns:
        String.
    """
    if type(vector_path) is not gpd.geodataframe.GeoDataFrame:
        input_vector = gpd.read_file(vector_path)
    else:
        input_vector = vector_path

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
