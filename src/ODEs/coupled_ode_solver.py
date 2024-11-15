""" 
Solve Coupled ODEs

YouTube tutorial: https://www.youtube.com/watch?v=MXUMJMrX2Gw

"""
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def odes(x, t):
    # constants
    a1 = 3e5
    a2 = 0.2
    a3 = 4e-7
    a4 = 0.6
    a5 = 8
    a6 = 90
    
    # Assign each ODE to a Vector Element
    A, B, C = x[0], x[1], x[2]
    
    # Define each ODE
    dA_dt = a1 - a2*A - a3*A*C
    dB_dt = a3*A*C - a4*B
    dC_dt = -a3*A*C - a5*C + a6*B
    
    return [dA_dt, dB_dt, dC_dt]

# Initial Conditions for ODEs
x0 = [2e6, 0, 90]

# Test the defined ODEs
# print(odes(x=x0, t=0))

# Declar a Time Vector (time window)
t = np.linspace(start=0, stop=15, num=1000)
x = odeint(odes, x0, t)

# ODEint returns a matrix x which has the solutions to the 
# different variables
A = x[:, 0]
B = x[:, 1]
C = x[:, 2]

# Plot
plt.semilogy(t, A, label='A')
plt.semilogy(t, B, label='B')  
plt.semilogy(t, C, label='C')  
plt.legend()
plt.show()
