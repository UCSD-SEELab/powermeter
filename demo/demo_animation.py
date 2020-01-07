#!/usr/bin/python

'''
An animation demo for powermeter
'''
import os
import time

from powermeter import PowerMeter

PWR_FILE = "./power.txt"
MEASURE_TIME = 120
MSG = "Collecting power measurements for {} seconds...\r\n".format(
        MEASURE_TIME)
MSG += "Check {} for detailed traces afterwards.".format(PWR_FILE)

def pwr_callback(pwr):
    '''
    Callback function that reads power from module.
    This function is responsible for recording time stamps
    that receive the power measurements.

    Args:
        pwr (float): the power measurement in W.

    Attributes:
        pwr_callback.start_time (float): the time that first data comes in, seconds
        pwr_callback.pwr_data: [time stamp (s), power (W)]
    '''
    if pwr_callback.start_time is None:
        pwr_callback.start_time = time.time() * 1000 # in ms

    pwr_callback.pwr_data.append(
        [float(time.time() * 1000 - pwr_callback.start_time) / 1000, pwr]
    )

pwr_callback.pwr_data = []
pwr_callback.start_time = None

def ina219_callback(pwr):
    '''
    Callback function that reads power from ina219.
    This function is responsible for recording time stamps
    that receive the power measurements.

    Args:
        pwr (float): the power measurement in W.

    Attributes:
        ina219_callback.start_time (float): the time that first data comes in, seconds
        ina219_callback.pwr_data: [time stamp (s), power (W)]
    '''
    if ina219_callback.start_time is None:
        ina219_callback.start_time = time.time() * 1000 # in ms

    ina219_callback.ina219_data.append(
        [float(time.time() * 1000 - pwr_callback.start_time) / 1000, pwr]
    )

ina219_callback.ina219_data = []
ina219_callback.start_time = None


def animate_plot(plot_types, max_time):
    '''
    Animation plot function.

    Args:
        plot_types (list): name of each plot type.
        max_time: maximum time range from 0.0 secs in secs.
    '''
    num_plots = len(plot_types)
    fig, ax = plt.subplots(num_plots, figsize=(12, 8))

    ax_dict = dict()
    plot_idx = 0
    for type_name in plot_types:
        ax_dict[type_name] = ax[plot_idx]
        plot_idx += 1

    ts = np.arange(0, max_time, 0.1)
    # NEED TO BE MANNUALLY SET
    line1, = ax_dict["powermeter"].plot(ts, [0.0] * len(ts), color="b")
    line2, = ax_dict["ina219"].plot(ts, [0.0] * len(ts), color="r")

    def animate(i):
        # prepare dataset and mannually set x and y axis
        powermeter_array = np.array(list(pwr_callback.pwr_data))
        ina219_array = np.array(list(ina219_callback.ina219_data))
        # print(powermeter_array.shape)
        # print(ina219_array.shape)

        if len(powermeter_array) == 0 or len(ina219_array) == 0:
            return line1, line2

        line1.set_xdata(powermeter_array[:,0])
        line1.set_ydata(powermeter_array[:,1])

        line2.set_xdata(ina219_array[:,0])
        line2.set_ydata(ina219_array[:,1])

        return line1, line2

    def init():
        return line1, line2

    ani = animation.FuncAnimation(
            fig, animate, np.arange(1, 1000), init_func=init,
            interval=500, blit=True) # 1000 frames

    # NEED TO BE MANNUALLY SET
    ax_dict["powermeter"].set_xlim(0.0, max_time)
    ax_dict["powermeter"].set_ylim(400.0, 550.0)
    ax_dict["powermeter"].set_title("Power traces measured by powermeter")
    ax_dict["powermeter"].set_ylabel("Power (W)")

    ax_dict["ina219"].set_xlim(0.0, max_time)
    ax_dict["ina219"].set_ylim(0.0, 100000000.00)
    ax_dict["ina219"].set_title("Power traces measured by INA219")
    ax_dict["ina219"].set_ylabel("Power (W)")

    plt.xlabel("Time (sec)")
    plt.tight_layout(pad=0.0, w_pad=0.0, h_pad=0.0)

    plt.show()

def main():
    '''
    main function
    Start measurement for 10s, save traces to PWR_FILE,
    and return all power values in pwr_callback.pwr_data.
    '''
    pm = PowerMeter(PWR_FILE)
    pm.run(pwr_callback)

    print(MSG)
    # Specify each plot and time range
    PLOT_TYPES = ["powermeter", "ina219"]
    MAX_TIME = 120.0
    animate_plot(PLOT_TYPES, MAX_TIME)
    time.sleep(MEASURE_TIME)

    pm.stop()

    for p in pwr_callback.pwr_data:
        print(p)

if __name__ == '__main__':
    main()
