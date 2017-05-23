#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created at 23 mai 2017 01:03
# created by Nil-Zil

from avec import *
import os
from matplotlib.font_manager import FontProperties
cm = plt.get_cmap('tab20')
colors = iter(cm(np.linspace(0, 1, 5)))  # "color" iterator
# "marker" iterator
# markers = iter([",", "o", "^", "*", "x", ">", "<", "^", "v"])
list_iter = iter(["abc", "abg"])  # list iterator

my_path = os.path.abspath(__file__ + "/../../../Report/Images/")


class Plot(object):
    def __init__(self):
        self.avec = LatticeParameter("avec")
        self.avec.setup()

    def plot_options(self, fig, ax, option):
        if option is "abc":
            self.avec.plot_a(fig, ax)
            self.avec.plot_b(fig, ax)
            self.avec.plot_c(fig, ax)
            self.avec.plot_limitline_abc(fig, ax)
            for i in range(2):
                plt.gca().get_lines()[i + 3].set_linestyle('dashdot')
        elif option is "abg":
            self.avec.plot_alpha(fig, ax)
            self.avec.plot_beta(fig, ax)
            self.avec.plot_gamma(fig, ax)
        else:
            print("Unknown option!")

    def plot_avec(self):
        fig, ax = plt.subplots()
        opt = next(list_iter)
        self.plot_options(fig, ax, opt)
        for i in range(3):
            # plt.gca().get_lines()[i].set_marker(next(markers))
            # plt.gca().get_lines()[i].set_markersize(1.5)
            # plt.gca().get_lines()[i].set_alpha(1)
            plt.gca().get_lines()[i].set_color(next(colors))

        ymin, ymax = self.avec.range_abc()
        ax.set_ylim((ymin - 1, ymax + 1))
        ax.set_xlabel("timestep", fontsize=12)
        ax.set_ylabel("cell vectors (a.u.)", fontsize=12)

        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.2,
                         box.width, box.height * 0.8])
        fontP = FontProperties()
        fontP.set_size('small')
        ax.legend(loc='center', bbox_to_anchor=(0.5, -0.3), ncol=3, prop=fontP)
        # plt.show()
        fig.savefig(my_path + "/input1/avec_" + str(opt) + ".pdf")


plot = Plot()
plot.plot_avec()
