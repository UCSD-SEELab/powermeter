# powermeter

This is a Python module for the HIOKI 3334 power meter in SEELab.

## Installation

Download the desired version from the release page and decompress it. `cd` into it, then:

```shell
# for v1.0 and Python 2.7
pip2 install .
# or for v2.0 and Python 3.5
pip3 install .
```

Note that v1.0 works for Python 2.7, while the current version in this repo (v2.0) supports Python 3.5.

By default, the module will be installed to your packages library for Python. However, if you do want to install the module in "editable" mode, which will be based on the code in the current directory:

```shell
# for v1.0 and Python 2.7
pip2 install -e .
# or for v2.0 and Python 3.5
pip3 install -e .
```

## Demo

A [simple demo](./demo/demo_simple.py) is included for reference.

In the demo, detailed traces will be saved to a text file, while a `callback` function is used to receive time-power tuples. The default units for time and power are **Seconds** and **Watts** respectively. 