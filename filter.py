#!/usr/bin/env python3

import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

GRAVITY = 9.81 # m/s^2
k = 1000 # (m/s)^2
ball_width = 1.0

def derivative(state, t):
    x, y, vx, vy = state
    if(y < ball_width):
        # force at y == ball_width = 0
        # force at y = 0 is infinite
        return [vx, vy, 0, 1000 * (ball_width - y) - GRAVITY]
    else:
        return [vx, vy, 0, -GRAVITY]

initial_state = [0, 10, 1, 0]
time_steps = np.linspace(0, 10, 1000)

states = integrate.odeint(derivative, initial_state, time_steps)

x, y, _, _ = states.T

fig, ax = plt.subplots()
ax.plot(x, y)
plt.grid(True)
plt.show()
