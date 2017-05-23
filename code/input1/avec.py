#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created at 23 mai 2017 00:57
# created by Nil-Zil

import numpy as np
import matplotlib.pyplot as plt
import csv


class LatticeParameter(object):
    def __init__(self, filename):
        self.timestep = []
        self.a = []
        self.b = []
        self.c = []
        self.alpha = []
        self.beta = []
        self.gamma = []
        with open(filename) as f:
            c = csv.reader(f, delimiter=' ', skipinitialspace=True)
            self.lines = []
            for line in c:
                self.lines.append([np.float64(string) for string in line])

    def extract_timestep(self):
        for line in self.lines:
            self.timestep.append(line[-1])

    def extract_a(self):
        for line in self.lines:
            self.a.append(line[0])

    def extract_b(self):
        for line in self.lines:
            self.b.append(line[1])

    def extract_c(self):
        for line in self.lines:
            self.c.append(line[2])

    def extract_alpha(self):
        for line in self.lines:
            self.alpha.append(line[3])

    def extract_beta(self):
        for line in self.lines:
            self.beta.append(line[4])

    def extract_gamma(self):
        for line in self.lines:
            self.gamma.append(line[5])

    def setup(self):
        self.extract_timestep()
        self.extract_a()
        self.extract_b()
        self.extract_c()
        self.extract_alpha()
        self.extract_beta()
        self.extract_gamma()

    def plot_a(self, fig, ax):
        ax.plot(self.timestep, self.a, label="a")

    def plot_b(self, fig, ax):
        ax.plot(self.timestep, self.b, label="b")

    def plot_c(self, fig, ax):
        ax.plot(self.timestep, self.c, label="c")

    def range_abc(self):
        amin, amax = min(self.a), max(self.a)
        bmin, bmax = min(self.b), max(self.b)
        cmin, cmax = min(self.c), max(self.c)
        pmin, pmax = min([amin, bmin, cmin]), max([amax, bmax, cmax])
        return pmin, pmax

    def plot_limitline_abc(self, fig, ax):
        lower_limit, upper_limit = self.range_abc()
        ax.plot([self.timestep[0], self.timestep[-1]],
                [lower_limit, lower_limit])
        ax.plot([self.timestep[0], self.timestep[-1]],
                [upper_limit, upper_limit])
