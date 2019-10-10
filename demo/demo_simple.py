#!/usr/bin/python

"""
A simple power reading demo for powermeter
"""
import os
import time

from powermeter import PowerMeter

PWR_FILE = "./power.txt"
MEASURE_TIME = 30

"""
Callback function that reads power from module.
This function is responsible for recording time stamps
that receive the power measurements.

Args:
    pwr (float): the power measurement in mW.
"""
def pwr_callback(pwr):
    if pwr_callback.start_time is None:
        pwr_callback.start_time = time.time() * 1000

    pwr_callback.pwr_data.append(
        [float(time.time * 1000 - pwr_callback.start_time), pwr]
    )

pwr_callback.pwr_data = []
pwr_callback.start_time = None

"""
main
Start measurement for 30s, save traces to PWR_FILE,
and return all power values in pwr_callback.pwr_data.
"""
def main():
    pm = PowerMeter(PWR_FILE)
    pm.run(pwr_callback)

    time.sleep(MEASURE_TIME)

    pm.stop()
    print(pwr_callback.pwr_data)

if __name__ == '__main__':
