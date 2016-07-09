#!/usr/bin/env python3

import matplotlib.pyplot as plt


def simple_step(delta_t):
    GRAV = 1 # G m1 m2
    # x y vx vy
    state = (1, 0, 0, 1)
    t = 0
    while True:
        yield t, state
        mag = sum(u**2 for u in state[0:2])**0.5

        # a = G m1 m2 / mag^2
        acceleration = tuple(-u * GRAV / mag**1.5 for u in state[0:2])

        velocity = (state[2] + acceleration[0] * delta_t,
                    state[3] + acceleration[1] * delta_t)

        # x + vx * dt + 0.5 * ax * dt^2
        update_pos = (u + vel * delta_t + 0.5 * acc * delta_t**2
                      for u, vel, acc in zip(state, velocity, acceleration))

        state = tuple( update_pos ) + tuple( velocity )
        t += delta_t

if __name__ == '__main__':
    states = []

    for t, state in simple_step(0.1):
        states.append(state)
        if t > 10:
            break

    fig, ax = plt.subplots()
    x = tuple(s[0] for s in states)
    y = tuple(s[1] for s in states)
    ax.plot(x, y, 'bo')
    plt.grid(True)
    plt.axis('equal')
    plt.show()
