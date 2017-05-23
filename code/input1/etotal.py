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
            if self.total_energy[i] - (self.total_kinetic[i] + self.total_potential[i]) < 1e-14:
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
            print("Energies mismatch!")

    def plot_total_energy(self, fig, ax):
        ax.plot(self.timestep, self.total_energy,
                label="total energy")

    def plot_total_kinetic(self, fig, ax):
        ax.plot(self.timestep, self.total_kinetic,
                label="total kinetic energy")

    def plot_total_potential(self, fig, ax):
        ax.plot(self.timestep, self.total_potential,
                label="total potential")

    def range_total(self):
        tmin, tmax = min(self.total_energy), max(self.total_energy)
        tkmin, tkmax = min(self.total_kinetic), max(self.total_kinetic)
        tpmin, tpmax = min(self.total_potential), max(self.total_potential)
        emin, emax = min([tmin, tkmin, tpmin]), max([tmax, tkmax, tpmax])
        return [emin, emax, tmin, tmax, tkmin, tkmax, tpmin, tpmax]

    def plot_limitline_total(self, fig, ax):
        # lower_total, upper_total = self.range_total()[2:4]
        lower_kinetic, upper_kinetic = self.range_total()[4:6]
        lower_potential, upper_potential = self.range_total()[6:8]
        # ax.plot([self.timestep[0], self.timestep[-1]],
        #         [lower_total, lower_total])
        # ax.plot([self.timestep[0], self.timestep[-1]],
        #         [upper_total, upper_total])
        ax.plot([self.timestep[0], self.timestep[-1]],
                [lower_kinetic, lower_kinetic])
        ax.plot([self.timestep[0], self.timestep[-1]],
                [upper_kinetic, upper_kinetic])
        ax.plot([self.timestep[0], self.timestep[-1]],
                [lower_potential, lower_potential])
        ax.plot([self.timestep[0], self.timestep[-1]],
                [upper_potential, upper_potential])
