# Based on https://github.com/pypa/sampleproject/blob/main/setup.py

from importlib.metadata import entry_points
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup (
    name="changesetdb",
    version="0.0.1",
    description="A command-line utilities to load OpenStreetMap changeset data into a PostgreSQL database",

    # Use README.md as the long description
    long_description=(here / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/pnorman/changesetdb",
    author="Paul Norman",
    author_email="osm@paulnorman.ca",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: GIS"
    ],
    keywords="openstreetmap, osm",
    packages=find_packages(),
    python_requires=">=3.9, <4",
    install_requires=[
        "Click",
        "psycopg[pool]"
    ],
    extras_require={
        "test": ["pytest"]
    },
    setup_requires=["flake8"],
    entry_points={
        "console_scripts": ["changesetdb = changesetdb.scripts:cli"]
    },
    project_urls={
        "Bug Reports": "https://github.com/pnorman/changesetdb/issues",
        "Source": "https://github.com/pnorman/changesetdb/",
    }
)
