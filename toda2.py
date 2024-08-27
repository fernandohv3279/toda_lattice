import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

from scipy.linalg import expm
from scipy.integrate import solve_ivp

L0=np.array([[  2,   1, 0.5],
             [  1,   3,0.25],
             [0.5,0.25,   4]])

A1=expm(L0)

a1=L0[0,0]
a2=L0[1,1]
a3=L0[2,2]

b1=L0[1,0]
b2=L0[1,2]
b3=L0[2,0]

p1=2*a1
p2=2*a2
p3=2*a3

b1=0.5*np.exp(-0.5*1)
b2=0.5*np.exp(-0.5*2)
b3=0.5*np.exp(-0.5*-3)

def toda_flow(t, y): return [y[3],y[4],y[5],
                             np.exp(-(y[0]-y[2]))-np.exp(-(y[1]-y[0])),
                             np.exp(-(y[1]-y[0]))-np.exp(-(y[2]-y[1])),
                             np.exp(-(y[2]-y[1]))-np.exp(-(y[0]-y[2]))
                             ]

# Fix this!!
# def flaschka(t, y): return [2*(y[3]*y[3]-y[0]*y[0]),
#                             2*(y[0]*y[0]-y[1]*y[1]),
#                             2*(y[1]*y[1]-y[2]*y[2]),
#                             y[10]*(y[1]*y[1]-y[2]*y[2]),
#                             y[4],y[5],
#                              np.exp(-(y[0]-y[2]))-np.exp(-(y[1]-y[0])),
#                              np.exp(-(y[1]-y[0]))-np.exp(-(y[2]-y[1])),
#                              np.exp(-(y[2]-y[1]))-np.exp(-(y[0]-y[2]))
#                              ]

finalTime=200
sol = solve_ivp(toda_flow, [0,finalTime], [0,0,0,2*L0[0,0],2*L0[1,1],2*L0[2,2]],dense_output=True)

t = np.linspace(0, finalTime, finalTime+1)
fig, ax = plt.subplots()

#ANIMATION

# For testing
z = sol.sol(t)[3:]
ax.plot(t, 0.5*z.T)

plt.show()
