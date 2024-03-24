import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

# Functions and Constants
DPi = 2 * np.pi
N = 4
NPi = N * np.pi
#!#

# Build

#!#

# Plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Prepare arrays x, y, z
k = np.linspace(0, 1, 100)

x = k
y = np.cos(k*NPi)
z = np.sin(k*NPi)

heli, = ax.plot(x, y, z)

##def update_lines(i):
##    k = np.linspace(-2, 2, 100)
##    heli.set_ydata(np.cos(theta) + i/50)
##    heli.set_xdata(np.sin(theta) + i/50)
##    return heli
##
##ani = animation.FuncAnimation(
##    fig, update_lines, interval=20, blit=True, save_count=10)

plt.show()
#!#
