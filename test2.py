import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# make up some data
x = [datetime.datetime.now() + datetime.timedelta(minutes=i) for i in range(12)]
y = [i+random.gauss(0,1) for i,_ in enumerate(x)]

# plot
fig, ax = plt.subplots()
ax.plot(x, y)

# beautifying the figure
minutes = mdates.MinuteLocator(interval = 2)
h_fmt   = mdates.DateFormatter('%H:%M:%S')
ax.xaxis.set_major_locator(minutes)
ax.xaxis.set_major_formatter(h_fmt)

fig.autofmt_xdate()

plt.show()
plt.close()