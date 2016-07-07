#!/usr/bin/env python3

import matplotlib.pyplot as plt


def simple_step(delta_t):
    GRAV = 10
    state = (10, 0, 0, 10)
    while True:
        yield state
        mag = sum(u**2 for u in state[0:2])**0.5

        acceleration = tuple(-u * GRAV / mag**1.5 for u in state[0:2])

        velocity = (state[2] + acceleration[0] * delta_t,
                    state[3] + acceleration[1] * delta_t)

        update_pos = (u + vel * delta_t + 0.5 * acc * delta_t**2
                      for u, vel, acc in zip(state, velocity, acceleration))

        state = tuple( update_pos ) + tuple( velocity )

if __name__ == '__main__':
    states = []

    for i, state in enumerate(simple_step(0.5)):
        states.append(state)
        if i > 50:
            break

    fig, ax = plt.subplots()
    x = tuple(s[0] for s in states)
    y = tuple(s[1] for s in states)
    ax.plot(x, y, 'bo')
    plt.grid(True)
    plt.axis('equal')
    plt.show()
