"""Tests for `utm_epsg_finder` module."""
from pathlib import Path

from utm_epsg_finder.utm_epsg_finder import (
    line_find_utm_epsg,
    point_find_utm_epsg,
    polygon_find_utm_epsg,
    raster_find_utm_epsg,
)

input_data_path = Path(__file__).parent.parent.parent.parent.parent
line = str(input_data_path / "test-data/input-data/line/line3857.shp")
point = str(input_data_path / "test-data/input-data/point/point.shp")
polygon = str(input_data_path / "test-data/input-data/atrani/atrani.geojson")
raster = str(input_data_path / "test-data/input-data/atrani/ndvi_atrani.tif")


def test_line_find_utm_epsg(tmp_path: Path) -> None:
    """Test on line_find_utm_epsg."""
    line_find_utm_epsg(input_data_path=line)


def test_point_find_utm_epsg(tmp_path: Path) -> None:
    """Test on polygon_find_utm_epsg."""
    point_find_utm_epsg(input_data_path=point)


def test_polygon_find_utm_epsg(tmp_path: Path) -> None:
    """Test on polygon_find_utm_epsg."""
    polygon_find_utm_epsg(input_data_path=polygon)


def test_raster_find_utm_epsg(tmp_path: Path) -> None:
    """Test on raster_find_utm_epsg."""
    raster_find_utm_epsg(input_data_path=raster)
