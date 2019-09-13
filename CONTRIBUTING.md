# MANTA Development

# Installing from the repository

To install a developer version of manta:

1. Clone this repository onto your local machine.
2. Navigate to your copy of repository (so that you're in same the directory that this README file is is).
3. Install using `pip install -e .`.
4. Install PyQt5 using `pip install pyqt5` or any other method.

# Packaging for PyPi

Before you do this, make sure everything's working correctly.
You can only upload a specific version **once**.
(You can also upload to a test repository, using `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`)

1. Create a "wheel", using `python setup.py sdist bdist_wheel`
2. Upload with `twine upload dist/*`

Verify that everything's working:

1. Go to some folder where manta isn't installed
2. Create a virtual environment: `virtualenv venv`
3. Activate it: `source venv/bin/activate`
4. Install PyQt5 and manta into the virtual environment: `pip install pyqt manta_maastricht`
5. Run with `manta` or `python -m manta_maastricht`

