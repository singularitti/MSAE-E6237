#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created at 10 avr. 2017 03:24
# created by Nil-Zil

import numpy as np
import matplotlib.pyplot as plt

sigma_ar = 3.405e-10
epsilon_ar = 1.654e-21


def lennard_johns_potential(r, sigma=sigma_ar, epsilon=epsilon_ar):
    tmp = (sigma / r)**6
    return 4 * epsilon * (tmp**2 - tmp)


def lennard_johns_force(r, sigma=sigma_ar, epsilon=epsilon_ar):
    tmp = sigma / r
    return 24 * epsilon / sigma * (2 * tmp**13 - tmp)


r = np.linspace(0.5e-10, 2e-10, num=500)
fig, ax1 = plt.subplots()
line1, = ax1.plot(r, [lennard_johns_potential(rr)
                      for rr in r], 'r-')
ax1.set_ylim((-1e-12, 1e-11))
ax1.set_xlabel("$r$", fontsize=12)
ax1.set_ylabel("$U(r)$", fontsize=12)

ax2 = ax1.twinx()
line2, = ax2.plot(r, [lennard_johns_force(rr)
                      for rr in r], 'g-')
ax2.set_ylim((-2, 16))
ax2.set_ylabel("$F(r)$", fontsize=12)
plt.legend((line1, line2), ("Lennard-Jones potential", "Lennard-Jones force"))

fig.tight_layout()
# plt.show()
fig.savefig("images/lj_ar.pdf")
