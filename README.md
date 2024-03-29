# Maastricht antiarrhythmic drug evaluator (MANTA)

This page (will soon contain) the source code for MANTA: a computational tool for better understanding of antiarrhythmic drugs.
MANTA is developed in [Jordi Heijman's Lab](http://www.jordiheijman.net/).

For details about MANTA, please see our publication in [Pharmacological Research](https://doi.org/10.1016/j.phrs.2019.104444) (open access).

To cite MANTA, please see the instructions [here](./CITATION).


## Quick installation

To install MANTA, use
```
pip install pyqt5 manta_maastricht
```

If you're using Python2, you might need to use
```
pip install manta_maastricht
```
and install PyQt5 some other way.
On certain Python distributions (e.g. Anaconda) it might already be provided.


## Running

To run, simply type
```
manta
```
or use the longer form
```
python -m manta_maastricht
```

For a user guide, please see the [supporting material to our publication](https://doi.org/10.1016/j.phrs.2019.104444).


## For developers

Some instructions for developers (including installating from the repo) are given in [CONTRIBUTING.md](./CONTRIBUTING.md).
