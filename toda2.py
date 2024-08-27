import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

from scipy.linalg import expm
from scipy.integrate import solve_ivp

q10=0
q20=-2*np.log(2)
q30=0

p10=4
p20=6
p30=8

def toda_flow(t, y):
    q1=y[0]
    q2=y[1]
    q3=y[2]
    p1=y[3]
    p2=y[4]
    p3=y[5]
    return [p1,p2,p3,
           np.exp(-(q1-q3))-np.exp(-(q2-q1)),
           np.exp(-(q2-q1))-np.exp(-(q3-q2)),
           np.exp(-(q3-q2))-np.exp(-(q1-q3))]

initial_condition=[q10,q20,q30,p10,p20,p30]
final_time=10
sol = solve_ivp(toda_flow, [0,final_time], initial_condition,dense_output=True)
t = range(final_time)
z = sol.sol(t)

def L(y):
    a1=0.5*y[3]
    a2=0.5*y[4]
    a3=0.5*y[5]
    b1=0.5*np.exp(-0.5*(y[1]-y[0]))
    b2=0.5*np.exp(-0.5*(y[2]-y[1]))
    b3=0.5*np.exp(-0.5*(y[0]-y[2]))
    return [[a1,b1,b3],
            [b1,a2,b2],
            [b3,b2,a3]]

for i in range(10):
    plt.plot(i,expm(L(z.T[i]))[0,0],'ro')

# #QR
# A=expm(L(z.T[0]))
# for i in t:
#     Q, R = np.linalg.qr(A)
#     A=np.matmul(R,Q)
#     plt.plot(i,A[0,0],'bo')
#     plt.plot(i,A[1,1],'bo')
#     plt.plot(i,A[2,2],'bo')

plt.show()
