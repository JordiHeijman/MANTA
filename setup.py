import sys
import os
from setuptools import setup, find_packages

setup(
    # Module name (lowercase)
    name='manta_maastricht',
    version='1.2',
    description='manta_maastricht',
    url='http://www.jordiheijman.net/',

    # Packages to exclude
    packages=find_packages(),
    zip_safe=False,

    # List of dependencies
    install_requires=[
        'myokit',
        #'PyQt5',
    ],

    # Register as a shell script
    entry_points = {
        'console_scripts': [
            'manta_maastricht-run=manta_maastricht.command_line:main',
        ],
    },

    # Include non-python files (via MANIFEST.in)
    include_package_data=True,
)
