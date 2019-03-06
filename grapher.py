import matplotlib.pyplot as plt
import csv_parser as csv_pr
from datetime import datetime
import numpy as np
import matplotlib.dates as mdates

def conv_24h(timestamp):
    dt = datetime.fromtimestamp(timestamp / (10 ** 6))
    return dt

def draw(Xparam, Yparam):
    Xdata = [(conv_24h(int(val))) for val in Xparam.data]
    Ydata = [float(val) for val in Yparam.data]

    plt.plot(Xdata, Ydata)

    plt.xlabel(Xparam.name)
    plt.ylabel(Yparam.name)

    plt.show()