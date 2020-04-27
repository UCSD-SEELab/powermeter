# powermeter

This is a Python module for the HIOKI 3334 power meter in SEELab.

## Installation

Download the desired version from the corresponding branch (`master` for Python >= 3.7, `py2.7` for Python >= 2.7) and decompress it. `cd` into it, then:

```shell
# for v1.0 and Python 2.7
pip2 install .
# or for v2.0 and Python 3.5
pip3 install .
```

By default, the module will be installed to your packages library for Python. However, if you do want to install the module in "editable" mode, which will be based on the code in the current directory:

```shell
# for v1.0 and Python 2.7
pip2 install -e .
# or for v2.0 and Python 3.5
pip3 install -e .
```

## Demos

There are several handy demos included in the `demo` folder:

* [simple demo](./demo/demo_simple.py)

This demo shows how to create a separate thread for power monitoring and how to receive data with a `callback` function. The measured traces ([time(s), power(mW)] pairs) will be logged into a text file.

* [animation demo](./demo/demo_animate.py)

This demo shows how to create a simple animation to view the power traces in real-time.

* [energy processing demo](./demo/demo_energy/)

This demo provides a processing script to calculate the energy for each phase based on the record time stamp.

## Notes

* The current version with animation and processing demos have not been thoroughly tested, thus the release is not ready. The prior release only includes the simple demo.