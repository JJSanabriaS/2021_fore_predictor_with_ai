import matplotlib.pyplot as plt
import datetime as dt
import fxcmpy

con = fxcmpy.fxcmpy(config_file='fxcm.cfg')
# must optain API Token, see link for details.

start = dt.datetime(2018, 7, 6,8,0,0)
end = dt.datetime(2018, 7, 7,18,0,0)

c = con.get_candles('XAU/USD', period='m1', columns=['bidclose','tickqty'], start=start, end=end )

# Basic plotting of close and volumne data

fig, ax = plt.subplots(figsize=(11,8))
ax.plot(c.index,c['bidclose'], lw=1, color='B',label="Close")
ax2= ax.twinx()
ax2.plot(c.index,c['tickqty'], lw=1, color='G',label="Volume")
plot.show()