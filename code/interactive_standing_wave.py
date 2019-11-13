import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# Set parameters
amplitude = 1
nodes = 2

# Normal plot
fig, ax = plt.subplots(1, 1)
x = np.linspace(0, 1, 1000)
y = amplitude*np.sin((nodes + 1)*np.pi*x)
sline, = ax.plot(x, y, lw=2)

ax.set_xlabel('$x$')
ax.set_ylabel('$f$')
ax.set_title(r"Standing wave with interior {} node(s), amplitude = {}".format(nodes, amplitude))
ax.set_ylim(-2, 2)

# Adjust plot to make room and add sliders
fig.subplots_adjust(left=0.15, bottom=0.25)

axcolor = 'gray'

amp_ax = plt.axes([0.05, 0.25, 0.01, 0.65], facecolor=axcolor)
node_ax = plt.axes([0.15, 0.15, 0.75, 0.02], facecolor=axcolor)

amp_slider = Slider(amp_ax, 'Amplitude',
                    valmin=0, valmax=2,
                    valinit=amplitude, valstep=0.1,
                    orientation='vertical')
node_slider = Slider(node_ax, 'Nodes',
                    valmin=0, valmax=10,
                    valinit=nodes, valstep=1)

# Animation update function
# This is called for each frame of the animation
def update(t):
    amplitude = amp_slider.val
    nodes = node_slider.val
    ax.set_title(r"Standing wave with interior {} node(s), amplitude = {}".format(nodes, amplitude))
    x = np.linspace(0, 1, 1000)
    y = amplitude*np.cos(2*np.pi*t)*np.sin((nodes + 1)*np.pi*x)
    sline.set_data(x, y)
    return (sline, )

# Setup and display the animation
anim = FuncAnimation(fig,
                    update,
                    frames=np.linspace(0, 1, 100),
                    interval=10,
                    repeat=True,
                    blit=True)

plt.show()

