#!/usr/bin/env python3
"""
Setup script for Katoolin3 - Allows installation via pip
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="katoolin3",
    version="1.0.0",
    author="MOG4125",
    description="Automatically install all Kali Linux tools on Windows and Linux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MOG4125/Katoolin3-4W",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Systems Administration",
    ],
    python_requires=">=3.10",
    package_data={
        "src": ["tools.json"],
    },
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "katoolin3=src.app:main",
        ],
    },
)
