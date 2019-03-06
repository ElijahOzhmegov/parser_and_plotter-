#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
# %matplotlib inline

#read data from csv
data = pd.read_csv('LD600.csv', sep=';', usecols=['Time','Depth'], parse_dates=['Time'])
#set date as index
data.set_index('Time',inplace=True)

#plot data
fig, ax = plt.subplots(figsize=(15,7))
# fig.autofmt_xdate()

# plt.show()

# plot
# fig, ax = plt.subplots()
# ax.plot(x, y)

# beautifying the figure
minutes = mdates.MinuteLocator(interval = 2)
h_fmt   = mdates.DateFormatter('%H:%M:%S')
ax.xaxis.set_major_locator(minutes)
ax.xaxis.set_major_formatter(h_fmt)

data.plot(ax=ax)
fig.autofmt_xdate()

plt.show()
plt.close()
