from setuptools import setup
import os

VERSION = "0.1a"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-basemap",
    description="A basemap for Datasette and datasette-leaflet",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-basemap",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-basemap/issues",
        "CI": "https://github.com/simonw/datasette-basemap/actions",
        "Changelog": "https://github.com/simonw/datasette-basemap/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_basemap"],
    entry_points={"datasette": ["basemap = datasette_basemap"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    tests_require=["datasette-basemap[test]"],
    package_data={"datasette_basemap": ["data/*"]},
    python_requires=">=3.6",
)
