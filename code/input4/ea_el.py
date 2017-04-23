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
        self.total_atom = []
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

    def extract_total_atom(self):
        for line in self.lines:
            self.total_atom.append(line[2])

    def check1(self):
        for i in range(len(self.timestep)):
            if self.total_atom[i] - (self.atom_kinetic[i] + self.atom_potential[i]) < 1e-14:
                return True
            else:
                return False

    def setup(self):
        self.extract_timestep()
        self.extract_total_atom()
        self.extract_atom_kinetic()
        self.extract_atom_potential()
        if self.check1():
            pass
        else:
            print("Atomic energies mismatch!")

    def plot_atom_energy(self, fig, ax, color):
        ax.plot(self.timestep, self.total_atom,
                label="total atomic energy", color=color, marker='^', markersize=1)

    def plot_atom_kinetic(self, fig, ax, color):
        ax.plot(self.timestep, self.atom_kinetic,
                label="atomic kinetic energy", color=color, marker='v', markersize=1)

    def plot_atom_potential(self, fig, ax, color):
        ax.plot(self.timestep, self.atom_potential,
                label="atomic potential", color=color, marker='o', markersize=1)


class LatticeEnergy(object):
    def __init__(self, filename):
        self.timestep = []
        self.lattice_potential = []
        self.lattice_kinetic = []
        self.total_lattice = []
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

    def extract_total_lattice(self):
        for line in self.lines:
            self.total_lattice.append(line[5])

    def check1(self):
        for i in range(len(self.timestep)):
            if self.total_lattice[i] - (self.lattice_kinetic[i] + self.lattice_potential[i]) < 1e-14:
                return True
            else:
                return False

    def setup(self):
        self.extract_timestep()
        self.extract_total_lattice()
        self.extract_lattice_kinetic()
        self.extract_lattice_potential()
        if self.check1():
            pass
        else:
            print("Lattice energies mismatch!")

    def plot_lattice_energy(self, fig, ax, color):
        ax.plot(self.timestep, self.total_lattice,
                label="total lattice energy", color=color)

    def plot_lattice_kinetic(self, fig, ax, color):
        ax.plot(self.timestep, self.lattice_kinetic,
                label="lattice kinetic energy", color=color)

    def plot_lattice_potential(self, fig, ax, color):
        ax.plot(self.timestep, self.lattice_potential,
                label="lattice potential")
