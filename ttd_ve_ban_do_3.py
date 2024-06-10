import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

xmin = 91
xmax = 562
ymin = 270
ymax = 570

fig, ax = plt.subplots()

px = [100, 500, 100]
py = [300, 450, 550]

lines, = ax.plot(px, py)
L = len(px)
N = 21
d = 100

lst_vi_tri_x=[]
lst_vi_tri_y=[]

for i in range(0, L-1):
    x1 = px[i]
    y1 = py[i]
    x2 = px[i+1]
    y2 = py[i+1]

    d0 = np.sqrt((x2-x1)**2+(y2-y1)**2)
    N0 = int(N*d0/d)
    dt = 1/(N0-1)
    for j in range(0, N0):
        t = j*dt
        x = x1+(x2-x1)*t
        y = y1+(y2-y1)*t
        lst_vi_tri_x.append(x)
        lst_vi_tri_y.append(y)

red_circle, =ax.plot([], [], 'ro',markersize=10)

FRAME =len(lst_vi_tri_x)

def init():
    ax.axis([xmin-70,xmax+70,ymin-70,ymax+70])
    # Trả về nhiều đoạn thẳng và đoạn thẳng tìm được
    return lines, red_circle 

def animate(i):
    red_circle.set_data(lst_vi_tri_x[i], lst_vi_tri_y[i])
    return lines, red_circle 

anim = FuncAnimation(fig, animate, frames=FRAME, interval=50, init_func=init, repeat=False)

plt.show()
