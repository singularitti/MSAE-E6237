#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created at Apr 22, 2017 18:23
# created by Nil-Zil

import numpy as np
import matplotlib.pyplot as plt
import csv


class AtomicEnergy(object):
    def __init__(self, filename):
        self.timestep = []
        self.atom_potential = []
        self.atom_kinetic = []
        self.atom_total = []
        with open(filename) as f:
            c = csv.reader(f, delimiter=' ', skipinitialspace=True)
            self.lines = []
            for line in c:
                self.lines.append([np.float64(string) for string in line])

    def extract_timestep(self):
        for line in self.lines:
            self.timestep.append(line[-1])

    def extract_atom_potential(self):
        for line in self.lines:
            self.atom_potential.append(line[0])

    def extract_atom_kinetic(self):
        for line in self.lines:
            self.atom_kinetic.append(line[1])

    def extract_atom_total(self):
        for line in self.lines:
            self.atom_total.append(line[2])

    def check1(self):
        for i in range(len(self.timestep)):
            if self.atom_total[i] - (self.atom_kinetic[i] + self.atom_potential[i]) < 1e-14:
                return True
            else:
                return False

    def setup(self):
        self.extract_timestep()
        self.extract_atom_total()
        self.extract_atom_kinetic()
        self.extract_atom_potential()
        if self.check1():
            pass
        else:
            print("Energies mismatch!")

    def plot_atom_energy(self, fig, ax):
        ax.plot(self.timestep, self.atom_total,
                label="total atomic energy")

    def plot_atom_kinetic(self, fig, ax):
        ax.plot(self.timestep, self.atom_kinetic,
                label="atomic kinetic energy")

    def plot_atom_potential(self, fig, ax):
        ax.plot(self.timestep, self.atom_potential,
                label="atomic potential")

    def range_atom(self):
        amin, amax = min(self.atom_total), max(self.atom_total)
        akmin, akmax = min(self.atom_kinetic), max(self.atom_kinetic)
        apmin, apmax = min(self.atom_potential), max(self.atom_potential)
        emin, emax = min([amin, akmin, apmin]), max([amax, akmax, apmax])
        return [emin, emax, amin, amax, akmin, akmax, apmin, apmax]

    def plot_limitline_atom(self, fig, ax):
        lower_total, upper_total = self.range_atom()[2:4]
        # lower_kinetic, upper_kinetic = self.range_atom()[4:6]
        # lower_potential, upper_potential = self.range_atom()[6:8]
        ax.plot([self.timestep[0], self.timestep[-1]],
                [lower_total, lower_total])
        ax.plot([self.timestep[0], self.timestep[-1]],
                [upper_total, upper_total])
        # ax.plot([self.timestep[0], self.timestep[-1]],
        #         [lower_kinetic, lower_kinetic])
        # ax.plot([self.timestep[0], self.timestep[-1]],
        #         [upper_kinetic, upper_kinetic])
        # ax.plot([self.timestep[0], self.timestep[-1]],
        #         [lower_potential, lower_potential])
        # ax.plot([self.timestep[0], self.timestep[-1]],
        #         [upper_potential, upper_potential])


class LatticeEnergy(object):
    def __init__(self, filename):
        self.timestep = []
        self.lattice_potential = []
        self.lattice_kinetic = []
        self.lattice_total = []
        with open(filename) as f:
            c = csv.reader(f, delimiter=' ', skipinitialspace=True)
            self.lines = []
            for line in c:
                self.lines.append([np.float64(string) for string in line])

    def extract_timestep(self):
        for line in self.lines:
            self.timestep.append(line[-1])

    def extract_lattice_potential(self):
        for line in self.lines:
            self.lattice_potential.append(line[3])

    def extract_lattice_kinetic(self):
        for line in self.lines:
            self.lattice_kinetic.append(line[4])

    def extract_lattice_total(self):
        for line in self.lines:
            self.lattice_total.append(line[5])

    def check1(self):
        for i in range(len(self.timestep)):
            if self.lattice_total[i] - (self.lattice_kinetic[i] + self.lattice_potential[i]) < 1e-14:
                return True
            else:
                return False

    def setup(self):
        self.extract_timestep()
        self.extract_lattice_total()
        self.extract_lattice_kinetic()
        self.extract_lattice_potential()
        if self.check1():
            pass
        else:
            print("Energies mismatch!")

    def plot_lattice_energy(self, fig, ax):
        ax.plot(self.timestep, self.lattice_total,
                label="total lattice energy")

    def plot_lattice_kinetic(self, fig, ax):
        ax.plot(self.timestep, self.lattice_kinetic,
                label="lattice kinetic energy")

    def plot_lattice_potential(self, fig, ax):
        ax.plot(self.timestep, self.lattice_potential,
                label="lattice potential")

    def range_lattice(self):
        lmin, lmax = min(self.lattice_total), max(self.lattice_total)
        lkmin, lkmax = min(self.lattice_kinetic), max(self.lattice_kinetic)
        lpmin, lpmax = min(self.lattice_potential), max(self.lattice_potential)
        emin, emax = min([lmin, lkmin, lpmin]), max([lmax, lkmax, lpmax])
        return [emin, emax, lmin, lmax, lkmin, lkmax, lpmin, lpmax]

    def plot_limitline_lattice(self, fig, ax):
        lower_total, upper_total = self.range_lattice()[2:4]
        # lower_kinetic, upper_kinetic = self.range_lattice()[4:6]
        # lower_potential, upper_potential = self.range_lattice()[6:8]
        ax.plot([self.timestep[0], self.timestep[-1]],
                [lower_total, lower_total])
        ax.plot([self.timestep[0], self.timestep[-1]],
                [upper_total, upper_total])
        # ax.plot([self.timestep[0], self.timestep[-1]],
        #         [lower_kinetic, lower_kinetic])
        # ax.plot([self.timestep[0], self.timestep[-1]],
        #         [upper_kinetic, upper_kinetic])
        # ax.plot([self.timestep[0], self.timestep[-1]],
        #         [lower_potential, lower_potential])
        # ax.plot([self.timestep[0], self.timestep[-1]],
        #         [upper_potential, upper_potential])
