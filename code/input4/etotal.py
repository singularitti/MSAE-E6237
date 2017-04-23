#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created at Apr 22, 2017 17:13
# created by Nil-Zil

import numpy as np
import matplotlib.pyplot as plt
import csv


class TotalEnergy(object):
    def __init__(self, filename):
        self.timestep = []
        self.total_potential = []
        self.total_kinetic = []
        self.total_energy = []
        with open(filename) as f:
            c = csv.reader(f, delimiter=' ', skipinitialspace=True)
            self.lines = []
            for line in c:
                self.lines.append([np.float64(string) for string in line])

    def extract_timestep(self):
        for line in self.lines:
            self.timestep.append(line[-1])

    def extract_total_potential(self):
        for line in self.lines:
            self.total_potential.append(line[0])

    def extract_total_kinetic(self):
        for line in self.lines:
            self.total_kinetic.append(line[1])

    def extract_total_energy(self):
        for line in self.lines:
            self.total_energy.append(line[2])

    def check1(self):
        for i in range(len(self.timestep)):
            if self.total_energy[i] - (self.total_kinetic[i] + self.total_potential[i]) < 1e-11:
                return True
            else:
                return False

    def setup(self):
        self.extract_timestep()
        self.extract_total_energy()
        self.extract_total_kinetic()
        self.extract_total_potential()
        if self.check1():
            pass
        else:
            print("Total energies mismatch!")

    def plot_total_energy(self, fig, ax, color):
        ax.plot(self.timestep, self.total_energy,
                label="total energy", color=color)

    def plot_total_kinetic(self, fig, ax, color):
        ax.plot(self.timestep, self.total_kinetic,
                label="total kinetic energy", color=color)

    def plot_total_potential(self, fig, ax, color):
        ax.plot(self.timestep, self.total_potential,
                label="total potential", color=color)
