========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/utm-epsg-finder/badge/?style=flat
    :target: https://readthedocs.org/projects/utm-epsg-finder
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/MaxDragonheart/utm-epsg-finder.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/MaxDragonheart/utm-epsg-finder

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/MaxDragonheart/utm-epsg-finder?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/MaxDragonheart/utm-epsg-finder

.. |requires| image:: https://requires.io/github/MaxDragonheart/utm-epsg-finder/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/MaxDragonheart/utm-epsg-finder/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/MaxDragonheart/utm-epsg-finder/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/MaxDragonheart/utm-epsg-finder

.. |version| image:: https://img.shields.io/pypi/v/utm-epsg-finder.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/utm-epsg-finder

.. |wheel| image:: https://img.shields.io/pypi/wheel/utm-epsg-finder.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/utm-epsg-finder

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/utm-epsg-finder.svg
    :alt: Supported versions
    :target: https://pypi.org/project/utm-epsg-finder

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/utm-epsg-finder.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/utm-epsg-finder

.. |commits-since| image:: https://img.shields.io/github/commits-since/MaxDragonheart/utm-epsg-finder/v0.0.2.svg
    :alt: Commits since latest release
    :target: https://github.com/MaxDragonheart/utm-epsg-finder/compare/v0.0.2...master



.. end-badges

Find EPSG code

* Free software: MIT license

Installation
============

::

    pip install utm-epsg-finder

You can also install the in-development version with::

    pip install https://github.com/MaxDragonheart/utm-epsg-finder/archive/master.zip


Documentation
=============


https://utm-epsg-finder.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
