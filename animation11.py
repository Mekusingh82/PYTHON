import numpy as np
import matplotlib.pyplot as ptl
import matplotlib.animation as animation

fig, ax = ptl.subplots()
x = np.linspace(0, 2 * np.pi, 200)
line, = ax.plot(x, np.sin(x))


def update(frame):
    line.set_ydata(np.sin(x + frame / 10.00))
    return line,

ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

ptl.show()