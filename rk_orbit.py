#!/usr/bin/env python3

import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

def rk_gen(f, delta_t, state):
    t = 0
    while True:
        yield(t, state)
        k1 = f(                t, state                     )
        k2 = f(t + 0.5 * delta_t, state + 0.5 * delta_t * k1)
        k3 = f(t + 0.5 * delta_t, state + 0.5 * delta_t * k2)
        k4 = f(t +       delta_t, state +       delta_t * k3)
        state = state + delta_t * (k1 + k2 + k3 + k4) / 6
        t += delta_t

def derivate(t, state):
    GRAVITY = 10
    mag = sum(float(u)**2 for u in state[0:2])**0.5
    acc = -state[0:2] * GRAVITY / mag**1.5
    return np.concatenate((state[2:4], acc))

if __name__ == '__main__':
    # state is (x, y, vx, vy)
    initial_state = np.matrix('10 0 0 10').transpose()
    states = []

    for i, (_, state) in enumerate(rk_gen(derivate, 0.5, initial_state)):
        states.append(state)
        if i > 50:
            break

    x = [float(s[0]) for s in states]
    y = [float(s[1]) for s in states]

    fig, ax = plt.subplots()
    ax.plot(x,y,'bo')
    plt.grid(True)
    plt.axis('equal')
    plt.show()
