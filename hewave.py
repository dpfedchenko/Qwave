import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

# Functions and Constants
DPi = 2 * np.pi
N = 5
NPi = N * np.pi
#!#

# Build

#!#

# Plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Prepare arrays x, y, z
##k = np.linspace(0, 1, 100)

rheli, = ax.plot([],[],[], color = 'red')
lheli, = ax.plot([],[],[], color = 'blue')

def update(i):
    k = np.linspace(0, 1, 100)
    rheli = ax.plot(k, np.cos(k*NPi - i/10), np.sin(k*NPi - i/10), color = 'red')
    lheli = ax.plot(k, np.cos(k*NPi + i/10), np.sin(k*NPi + i/10), color = 'blue')
    return rheli, lheli

ani = animation.FuncAnimation(
    fig,
    update,
    blit = True, save_count=10)

plt.show()
#!#
