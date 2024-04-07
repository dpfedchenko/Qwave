import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

# Fixing random state for reproducibility

def random_walk(num_steps, max_step=0.05):
    start_pos = (0.5,0.5,0.5)
    steps = np.random.uniform(-max_step, max_step, size=(num_steps, 3))
    print(type(steps))
    walk = start_pos + np.cumsum(steps, axis=0)
    print(type(walk))
    return walk

def update_lines(num, walks, lines):
    for line, walk in zip(lines, walks):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(walk[:num, :2].T)
        line.set_3d_properties(walk[:num, 2])
    return lines

# Data: 40 random walks as (num_steps, 3) arrays
num_steps = 10
walks = [random_walk(num_steps) for index in range(2)]
print(walks)


# Attaching 3D axis to the figure
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Create lines initially without data
lines = [ax.plot([], [], [])[0] for _ in walks]

# Creating the Animation object
ani = animation.FuncAnimation(
    fig, update_lines, num_steps, fargs=(walks, lines), interval=100)

plt.show()
