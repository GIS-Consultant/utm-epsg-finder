"""Tests for `utm_epsg_finder` module."""
from pathlib import Path

from utm_epsg_finder.utm_epsg_finder import polygon_find_utm_epsg

input_data_path = Path(__file__).parent.parent.parent.parent
input_vector = str(input_data_path / "test-data/input-data/atrani/atrani.geojson")


def test_polygon_find_utm_epsg(tmp_path: Path) -> None:
    """Test on polygon_find_utm_epsg."""
    polygon_find_utm_epsg(vector_path=input_vector)
