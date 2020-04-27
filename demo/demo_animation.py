#!/usr/bin/python3

'''
An animation demo that will display the readings from powermeter
'''
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import os
import time
from powermeter import PowerMeter

PWR_FILE = "./power.txt"
MEASURE_TIME = 1
SAMPLE_INTERVAL = 0

# x and y axis boundaries
MAX_TIME = 40.0 # seconds
MAX_POWER = 5 # W

def pwr_callback(pwr_data):
    '''
    Callback function that reads power data from module with continuous sampling
    Args:
        pwr_data : [time stamps(s), power(W)]
    Attributes:
        pwr_callback.start_time (float): the time that first data comes in, seconds
        pwr_callback.pwr_data: A list of [time stamp (s), power (W)]
    '''
    if pwr_callback.start_time is None:
        pwr_callback.start_time = time.time()

    pwr_callback.pwr_data.append([float(time.time() - pwr_callback.start_time), pwr_data])
pwr_callback.pwr_data = []
pwr_callback.start_time = None


def pwr_animation():
    '''
    Function that creates an animation to display the readings
    Args:
        pwr_data : [time stamps(s), power(W)]
    '''
    fig = plt.figure()
    ax = fig.gca()
    # default line, need to be mannually set
    ts = np.arange(0, MAX_TIME, 0.1)
    line, = ax.plot(ts, [0.0] * len(ts), color='b')

    def init():
        return line,

    def animate(i):
        '''
        Prepare dataset and mannually set x and y axis
        '''
        pwr_data = np.array(pwr_callback.pwr_data)
        if pwr_data.size == 0:
            return line,

        line.set_xdata(pwr_data[:, 0])
        line.set_ydata(pwr_data[:, 1])
        return line,


    pwr_ani = animation.FuncAnimation(fig, animate, np.arange(1, 1000), init_func=init,
         interval=200, blit=True) # 1000 frames

    ax.set_xlim(0, MAX_TIME)
    ax.set_ylim(0, MAX_POWER)
    ax.set_xlabel('time (s)')
    ax.set_ylabel('power (W)')
    ax.set_title('power reading with sampling interval {}ms'.format(SAMPLE_INTERVAL))
    plt.show()

def main():
    '''
    main function
    Generate an animation that displays readings in real time.
    '''
    pm = PowerMeter(PWR_FILE)
    pm.run(pwr_callback)
    pwr_animation()
    time.sleep(MEASURE_TIME)
    pm.stop()

if __name__ == '__main__':
    main()

