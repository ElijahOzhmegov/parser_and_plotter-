import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

idx = pd.date_range('2017-01-01 05:03', '2017-01-01 05:23', freq = 'min')

df = pd.DataFrame(np.cumsum(np.random.randn(len(idx), 2),0),
                  index = idx, columns=list("AB"))

fig, ax = plt.subplots()
ax.plot(df.index, df["A"], color = 'black')
ax2 = ax.twinx()
ax2.plot(df.index, df["B"], color = 'indigo')

minutes = mdates.MinuteLocator(interval = 3)
h_fmt   = mdates.DateFormatter('%H:%M:%S')
ax.xaxis.set_major_locator(minutes)
ax.xaxis.set_major_formatter(h_fmt)

fig.autofmt_xdate()
plt.show()