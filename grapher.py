from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv_parser as csv_pr
import numpy as np


def conv_24h(timestamp):
    dt = datetime.fromtimestamp(timestamp / (10 ** 6)) # convert to lambda function?
    return dt


def draw2(name, Xparam, Yparams): # make legend output? # make saving line charts as png files?
    fig = plt.figure(figsize=(16, 9))
    ax = fig.add_subplot(111)

    xlabel = Xparam.name
    ylabel = ""

    Xdata = [(conv_24h(int(val))) for val in Xparam.data] # Xdata is not always "datatime"?

    for Yparam in Yparams:
        Ydata = [float(val) for val in Yparam.data]
        ylabel = ylabel + " " + Yparam.name

        ax.plot(Xdata, Ydata)

    plt.title(name)
    plt.grid(True)

    h_fmt = mdates.DateFormatter('%H:%M:%S')
    ax.xaxis.set_major_formatter(h_fmt)
    _ = plt.xticks(rotation=40)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.show()


def draw(array_of_graphs, line_of_Parameters):

    for graph in array_of_graphs:
        name = graph.name

        Yparams =[]

        for param in line_of_Parameters:
            if param.name == graph.Xname:
                Xparam = param

            for gr_Yname in graph.Ynames:
                if param.name == gr_Yname:
                    Yparams.append(param)

        draw2(name, Xparam, Yparams)

