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
N = 2.5
#!#

# Plot
fig, ax = plt.subplots()
x = np.arange(0, N*DPi, h)

rline, = ax.plot(x, np.exp(I * x))
lline, = ax.plot(x, np.exp(I * x), color = 'red')

smline, = ax.plot(x, np.exp(I * x) - np.exp(-I * x),
                 color = 'green',
                 linewidth = 3)

spline, = ax.plot(x, np.exp(I * x) + np.exp(-I * x),
                 color = 'magenta',
                 linewidth = 3)

spectr, = ax.plot(x,
                 (np.exp(I * x) - np.exp(-I * x)).real + (np.exp(I * x) + np.exp(-I * x)).real,
                  color = 'orange',
                  linewidth = 5)

def animate(i):
    # k-vectors
    kr = 25
    kl = 25

    # Amplitudes
    Ar = 1#np.cos(i/50)
    Al = 1#np.sin(i/50)

    rline.set_ydata(Ar*np.exp(I*(x - i/kr)))
    lline.set_ydata(Al*np.exp(I*(x + i/kl)))

    E = Ar*np.exp(I*(x - i/kr)) - Al*np.exp(I*(x + i/kl))
    H = Ar*np.exp(I*(x - i/kr)) + Al*np.exp(I*(x + i/kl))

    smline.set_ydata(E)
    spline.set_ydata(H)

    return rline, lline, smline, spline

ani = animation.FuncAnimation(
    fig, animate, interval = 20, blit = True, save_count=10)

plt.show()
#!#
