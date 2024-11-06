# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:43:35 2024

@author: Cam Eldridge
"""

import matplotlib.pyplot as plt
import math

class Material:
    def __init__(self, density, resistivity, cost):
        self.density = density        # Density (kg/m^3)
        self.resistivity = resistivity  # Resistivity (Ohm-meter)
        self.conductivity = 1 / resistivity  # Conductivity
        self.cost = cost              # Cost in USD/kg

    def diameter(self, length, resistance):
        # Calculate the diameter of the wire
        area = self.resistivity * length / resistance
        dia = 2 * math.sqrt(area / math.pi)
        return dia

    def mass(self, length):
        # Calculate the mass of the wire
        area = self.resistivity * length / resistance
        mass = self.density * area * length
        return mass

    def material_cost(self, length):
        # Calculate the cost of the wire
        mass = self.mass(length)
        cost = self.cost * mass
        return cost

# Create material objects for Aluminum and Copper
aluminum = Material(2710, 2.65e-8, 2.66)
copper = Material(8960, 1.724e-8, 9.77)


voltage= 120    #Voltage in volts
losses= .2      #Loss tolerance in per cent
for i in range(1, 2401, 100):
    length = i  # Length of the wire in meters
    if length < 500:
        power=length*3
    else:
        power=length*2
    current = power/voltage
    resistance= losses*power/(current*current) # Desired resistance in Ohms


# Calculate and print results for Copper
print(f"Copper diameter is {copper.diameter(length, resistance):.4f}")
print(f"Copper mass is {copper.mass(length):.2f} kg")
print(f"Copper cost is {copper.material_cost(length):.2f} USD\n")

'''# Calculate and print results for Aluminum
print(f"Aluminum diameter is {aluminum.diameter(length, resistance):.4f} m")
print(f"Aluminum mass is {aluminum.mass(length):.2f} kg")
print(f"Aluminum cost is {aluminum.material_cost(length):.2f} USD")'''
