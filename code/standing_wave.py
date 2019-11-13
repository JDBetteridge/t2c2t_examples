import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

# Set parameters
amplitude = 1
nodes = 2

# Normal plot
fig, ax = plt.subplots(1, 1)
x = np.linspace(0, 1, 1000)
y = amplitude*np.sin((nodes + 1)*np.pi*x)
sline, = ax.plot(x, y)

# Animation update function
# This is called for each frame of the animation
def update(t):
    x = np.linspace(0, 1, 1000)
    y = amplitude*np.cos(2*np.pi*t)*np.sin((nodes + 1)*np.pi*x)
    sline.set_data(x, y)
    return (sline, )

# Initialization function
# Plots the first frame
def init():
    return update(0)
# add "init_func=init" to FuncAnimation

# Setup and display the animation
anim = FuncAnimation(fig,
                    update,
                    frames=np.linspace(0, 1, 100),
                    interval=10,
                    repeat=True,
                    blit=True)

plt.show()

