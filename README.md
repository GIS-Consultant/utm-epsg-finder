# UTM EPSG Finder
[![PyPI - Version](https://img.shields.io/pypi/v/utm-epsg-finder.svg)](https://pypi.python.org/pypi/utm-epsg-finder)
[![PyPI - License](https://img.shields.io/pypi/l/utm-epsg-finder.svg)](https://pypi.python.org/pypi/utm-epsg-finder)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/utm-epsg-finder.svg)](https://pypi.python.org/pypi/utm-epsg-finder)
[![Tests](https://github.com/GIS-Consultant/utm-epsg-finder/workflows/tests/badge.svg)](https://github.com/GIS-Consultant/utm-epsg-finder/actions?workflow=tests)
[![codecov](https://codecov.io/gh/GIS-Consultant/utm-epsg-finder/branch/master/graph/badge.svg?token=CFA8VDHT8W)](https://codecov.io/gh/GIS-Consultant/utm-epsg-finder)
[![Read the Docs](https://readthedocs.org/projects/utm-epsg-finder/badge/)](https://utm-epsg-finder.readthedocs.io/)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

## Description
**UTM EPSG Finder** allow the user to find the UTM's [EPSG](https://epsg.org/home.html) code from his vectors in [EPSG:4326](http://epsg.io/4326) and [ESPG:3857](http://epsg.io/3857).
Sometimes is useful to know the projected EPSG; as example when you will calculate the polygon's area or the distance between two points. In this case if your vectors are in 4326 or worst in 3857
you can't return a correct value. Remember that with Pseudo-Mercator is not optimal calculate area but if you use an UTM EPSG the output value from area calculation is more correct.

**UTM EPSG Finder** is based on:
- [GeoPandas](https://pypi.org/project/geopandas/)
- [pyproj](https://pypi.org/project/pyproj/)
- [shapely](https://shapely.readthedocs.io/en/latest/project.html)  
- [rasterio](https://rasterio.readthedocs.io/en/latest/index.html)
- [utm](https://pypi.org/project/utm/)


## Feature
- [x] Get UTM EPSG for lines
- [x] Get UTM EPSG for points
- [x] Get UTM EPSG for polygons
- [x] Get UTM EPSG for raster

## More
* GitHub repo: <https://github.com/GIS-Consultant/utm-epsg-finder.git>
* Documentation: <https://utm-epsg-finder.readthedocs.io>
* Free software: MIT


## Credits

This package was created with [Cookiecutter][cookiecutter] and the [fedejaure/cookiecutter-modern-pypackage][cookiecutter-modern-pypackage] project template.

[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[cookiecutter-modern-pypackage]: https://github.com/fedejaure/cookiecutter-modern-pypackage

Thanks to [g2giovanni](https://github.com/g2giovanni) for the help to setting up the package.
