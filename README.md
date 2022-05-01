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

* [ethernet power measurement demo](./demo/demo_ethernet.py/)

This demo assumes two RPis in the setup: one RPi for running the workloads, and the other RPi for measuring the power of that RPi.
Two RPis are connected via an Ethernet cable, where simple signals are sent to indicate the start and the end of the workload.

* [animation demo](./demo/demo_animation.py)

This demo shows how to create a simple animation to view the power traces in real-time.

* [energy processing demo](./demo/demo_process/)

This demo provides a processing script to calculate the energy for each phase based on the record time stamp.

## Notes

* The automatically generated log file `PWR_FILE` when creating the powermeter as `pm = PowerMeter(PWR_FILE)`, adopts the following format:
  ```
  time_stamp,volt,curr,pf,mul
  1651386186231,123.4,0.0625,0.512,3.9488000000000003
  1651386186276,123.4,0.0625,0.512,3.9488000000000003
  ...
  ```

  * `time_stamp`: the system sampling time in millisecond
  * `volt`: the votage in V
  * `curr`: the current in A
  * `pf`: the power factor which is a specific parameter for HIOKI 3334
  * `mul`: the measured power in W, which results from `volt*curr*pf`

## Cite the powermeter

```
@misc{hioki3334,
  title = {{Hioki3334 Powermeter}},
  howpublished = {\url{https://www.hioki.com/en/products/detail/?product_key=5812}},
}
```