"""Tests for `utm_epsg_finder` module."""
from typing import Generator

import pytest

import utm_epsg_finder


@pytest.fixture
def version() -> Generator[str, None, None]:
    """Sample pytest fixture."""
    yield utm_epsg_finder.__version__


def test_version(version: str) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    assert version == "0.0.2"
