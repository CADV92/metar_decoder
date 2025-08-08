#!/usr/bin/env python3
"""
Setup script para METAR Decoder
Instalación:
    pip install .
o en modo editable (desarrollo):
    pip install -e .
"""

from setuptools import setup, find_packages
from pathlib import Path

README = Path(__file__).with_name("README.md").read_text(encoding="utf-8")

setup(
    name="metar_decoder",
    version="0.1.0",
    author="Christian Dávila",
    author_email="cadv.met.92@gmail.com",
    description="Decodificador de mensajes METAR",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/CADV92/metar_decoder",
    project_urls={
        "Bug Tracker": "https://github.com/CADV92/metar_decoder/issues",
        "Source": "https://github.com/CADV92/metar_decoder",
    },
    license="MIT",
    keywords=[
        "metar", "aviation weather", "aeronautical meteorology",
        "SENAMHI", "weather", "parser"
    ],
    packages=find_packages(
        include=["metar_decoder", "metar_decoder.*"],
        exclude=["metar_decoder.tests", "metar_decoder.tests.*"]
    ),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "flake8",
            "mypy",
        ],
        "docs": [
            "sphinx",
            "sphinx-rtd-theme",
        ],
    },
    entry_points={
        "console_scripts": [
            "metar_decode=metar_decoder.cli:main",
        ],
    },
)