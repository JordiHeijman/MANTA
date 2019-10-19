import sys
import os
from setuptools import setup, find_packages

# One line description
short_description = '''
Maastricht antiarrhythmic drug evaluator (MANTA): a computational tool for
better understanding of antiarrhythmic drugs
'''.strip()

# Longer descripton
with open('README.md') as f:
    readme = f.read()

# Read version number from file
def load_version():
    try:
        import os
        root = os.path.abspath(os.path.dirname(__file__))
        with open(os.path.join(root, 'manta_maastricht', 'version'), 'r') as f:
            version = f.read().strip()
        parts = [int(x) for x in version.split('.')]
        if len(parts) != 3:
            raise Exception('Version number must have three parts.')
    except Exception as e:
        raise RuntimeError('Unable to read version number (' + str(e) + ').')

# Call setuptools
setup(
    # Module name (lowercase)
    name='manta_maastricht',

    # Version number
    version='1.1.5',

    # Descriptions
    url='http://www.jordiheijman.net/',
    description=short_description,
    long_description=readme,
    long_description_content_type='text/markdown',

    # Packages to include
    packages=find_packages(),

    # Include non-python files (via MANIFEST.in)
    zip_safe=False,
    include_package_data=True,

    # Register as a shell script
    entry_points = {
        'console_scripts': [
            'manta = manta_maastricht.__main__:main',
        ],
    },

    # List of dependencies
    install_requires=[
        'myokit',
        #'PyQt5',
    ],
)
