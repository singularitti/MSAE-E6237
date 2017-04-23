#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created at Apr 22, 2017 18:41
# created by Nil-Zil

from etotal import *
from ea_el import *
from matplotlib.font_manager import FontProperties
hsv = plt.get_cmap('hsv')
colors = hsv(np.linspace(0, 1, 9))


class Plot(object):
    def __init__(self):
        self.et = TotalEnergy("e")
        self.at = AtomicEnergy("eal")
        self.lt = LatticeEnergy("eal")
        self.et.setup()
        self.at.setup()
        self.lt.setup()

    def plot_e(self, option):
        fig, ax = plt.subplots()
        if option is "e":
            self.et.plot_total_energy(fig, ax, colors[0])
            self.et.plot_total_kinetic(fig, ax, colors[1])
            self.et.plot_total_potential(fig, ax, colors[2])
        elif option is "a":
            self.at.plot_atom_energy(fig, ax, colors[3])
            self.at.plot_atom_kinetic(fig, ax, colors[4])
            self.at.plot_atom_potential(fig, ax, colors[5])
        elif option is "l":
            self.lt.plot_lattice_energy(fig, ax, colors[6])
            self.lt.plot_lattice_kinetic(fig, ax, colors[7])
            self.lt.plot_lattice_potential(fig, ax, colors[8])
        else:
            print("Unknown option!")
        ax.set_ylim((-0.03, 0.01))
        ax.set_xlabel("timestep", fontsize=12)
        ax.set_ylabel("$\\varepsilon$", fontsize=12)

        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.2,
                         box.width, box.height * 0.8])
        fontP = FontProperties()
        fontP.set_size('small')
        ax.legend(loc='center', bbox_to_anchor=(0.5, -0.3), ncol=3, prop=fontP)
        # plt.show()
        fig.savefig(str(option) + ".pdf")


plot = Plot()
plot.plot_e("e")
plot.plot_e("a")
plot.plot_e("l")
