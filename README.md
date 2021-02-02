# datasette-basemap

[![PyPI](https://img.shields.io/pypi/v/datasette-basemap.svg)](https://pypi.org/project/datasette-basemap/)
[![Changelog](https://img.shields.io/github/v/release/simonw/datasette-basemap?include_prereleases&label=changelog)](https://github.com/simonw/datasette-basemap/releases)
[![Tests](https://github.com/simonw/datasette-basemap/workflows/Test/badge.svg)](https://github.com/simonw/datasette-basemap/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-basemap/blob/main/LICENSE)

A basemap for Datasette and datasette-leaflet

## Installation

Install this plugin in the same environment as Datasette.

    $ datasette install datasette-basemap

## Usage

This plugin will make a `basemap` database available containing OpenStreetMap tiles in the [mbtiles](https://github.com/mapbox/mbtiles-spec) format.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-basemap
    python3 -mvenv venv
    source venv/bin/activate

Or if you are using `pipenv`:

    pipenv shell

Now install the dependencies and tests:

    pip install -e '.[test]'

To run the tests:

    pytest
