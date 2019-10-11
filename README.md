# powermeter

This is a Python module for the HIOKI 3334 power meter in SEELab.

## Installation

Clone the latest release of this repository (or download its archive), `cd` into it, then:

```shell
pip2 install .
```

The current version (v1.0) works for Python 2.7.

By default, the module will be installed to your packages library for Python 2.7. However, if you do want to install the module in "editable" mode, which will be based on the code in the current directory:

```shell
pip2 install -e .
```

## Demo

A [simple demo](./demo/demo_simple.py) is included for reference.

In the demo, detailed traces will be saved to a text file, while a `callback` function is used to receive time-power tuples. The default units for time and power are **Seconds** and **Watts** respectively. 