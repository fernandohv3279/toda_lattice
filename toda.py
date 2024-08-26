import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def toda_flow(t, y): return [y[3],y[4],y[5],
                             np.exp(-(y[0]-y[2]))-np.exp(-(y[1]-y[0])),
                             np.exp(-(y[1]-y[0]))-np.exp(-(y[2]-y[1])),
                             np.exp(-(y[2]-y[1]))-np.exp(-(y[0]-y[2]))
                             ]

sol = solve_ivp(toda_flow, [0,10], [-1,-2.4,5,0,0,0],dense_output=True)

t = np.linspace(0, 10, 100)
fig, ax = plt.subplots()

p1 = sol.sol(t)[0]
p2 = sol.sol(t)[1]
p3 = sol.sol(t)[2]

#ANIMATION

# For testing
# z = sol.sol(t)[:3]
# ax.plot(t, z.T)

line1 = ax.plot(t[0], p1[0],'b')[0]
line2 = ax.plot(t[0], p2[0],'m')[0]
line3 = ax.plot(t[0], p3[0],'g')[0]
lastpoint1=ax.plot(t[0], p1[0],'bo')[0]
lastpoint2=ax.plot(t[0], p2[0],'mo')[0]
lastpoint3=ax.plot(t[0], p3[0],'go')[0]
ax.set(xlim=[-10, 10], ylim=[-10, 10], xlabel='Time', ylabel='Position')

def update(frame):

    line1.set_data(t[:frame],p1[:frame])
    line2.set_data(t[:frame],p2[:frame])
    line3.set_data(t[:frame],p3[:frame])

    lastpoint1.set_data([t[frame]], [p1[frame]])
    lastpoint2.set_data([t[frame]], [p2[frame]])
    lastpoint3.set_data([t[frame]], [p3[frame]])
    ax.set(xlim=[-10+frame*10/100, 10+frame*10/100])
    return (line1,line2,line3,lastpoint1,lastpoint2,lastpoint3)

ani = animation.FuncAnimation(fig=fig, func=update, frames=100, interval=40)
plt.show()
