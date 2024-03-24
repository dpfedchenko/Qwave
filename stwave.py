import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

# Functions and Constants
DPi = 2*np.pi
Pi = np.pi
I = complex(0, 1)
h = 0.1
#!#

# Build
N = 1.5
#!#

# Plot
fig, ax = plt.subplots()
x = np.arange(0, N*DPi, h)
rline, = ax.plot(x, np.exp(I * x))
lline, = ax.plot(x, np.exp(I * x), color = 'red')
sline, = ax.plot(x, np.exp(I * x) + np.exp(-I * x),
                 color = 'green')
def animate(i):
    A = 1#np.cos(i/50)
    B = 1#np.sin(i/50)
    rline.set_ydata(A*np.exp(I*(x - i/50)))  # update the data.
    lline.set_ydata(B*np.exp(I*(x + i/50)))  # update the data.
    sline.set_ydata(A*np.exp(I*(x - i/50)) + B*np.exp(I*(x + i/50)))  # update the data.
    return rline, lline, sline

ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=10)

plt.show()
#!#
