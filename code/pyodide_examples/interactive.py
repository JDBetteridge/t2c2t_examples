import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Do a "Regular" plot
fig, ax = plt.subplots(1, 1)

α = 0
ω = 1
t = np.linspace(0, 2*np.pi, 200)
lines, = ax.plot(t, (t**α)*np.sin(ω*t))

ax.set_xlabel('$t$')
ax.set_ylabel('$f$')
ax.set_title(r"$\alpha$ = {}, $\omega$ = {}".format(α, ω))

# Adjust plot to make room and add sliders
fig.subplots_adjust(left=0.1, bottom=0.25)

axcolor = 'gray'

alpha_ax = plt.axes([0.1, 0.10, 0.75, 0.02], facecolor=axcolor)
omega_ax = plt.axes([0.1, 0.05, 0.75, 0.02], facecolor=axcolor)

alpha_slider = Slider(alpha_ax, r'$\alpha$', valmin=0, valmax=2, valinit=α, valstep=0.1)
omega_slider = Slider(omega_ax, r'$\omega$', valmin=-10, valmax=+10, valinit=ω, valstep=0.1)
    
# Define an update function for when values change
def update(val):
    α = alpha_slider.val
    ω = omega_slider.val
    ax.set_title(r"$\alpha$ = {}, $\omega$ = {}".format(α, ω))
    lines.set_ydata((t**α)*np.sin(ω*t))
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw_idle()
    
# Set the update function for the sliders
alpha_slider.on_changed(update)
omega_slider.on_changed(update)

plt.show()

