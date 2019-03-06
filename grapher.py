import matplotlib.pyplot as plt
import csv_parser as csv_pr
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime

def conv_24h(timestamp):
    dt = datetime.fromtimestamp(timestamp / (10 ** 6))
    return dt

def draw(Xparam, Yparam):
    Xdata = [(conv_24h(int(val))) for val in Xparam.data]
    Ydata = [float(val) for val in Yparam.data]

    fig, ax = plt.subplots()
    ax.plot(Xdata, Ydata)

    h_fmt = mdates.DateFormatter('%H:%M:%S')
    ax.xaxis.set_major_formatter(h_fmt)
    _ = plt.xticks(rotation=30)

    plt.xlabel(Xparam.name)
    plt.ylabel(Yparam.name)

    plt.show()