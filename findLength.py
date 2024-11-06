# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:36:31 2024

@author: 2024
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
aluminum = Material(2710, 2.65e-8, 2.66)  # Aluminum material properties
copper = Material(8960, 1.724e-8, 9.77)   # Copper material properties

# Constants for power calculations
voltage = 120  # Voltage in volts
losses = 0.2   # Loss factor (fraction of voltage lost)

# Iterate through different wire lengths and calculate costs
for length in range(0, 2400, 100):  # Wire lengths from 0 to 2400 meters, step by 100
    if length < 500:
        power = length * 3  # Power for shorter lengths
    else:
        power = length * 2  # Power for longer lengths
        
    current = power / voltage  # Current (I = P / V)
    
    if current == 0:
        print("For 0 meters: no power") # Skipping the divide by zero case
        print("-" * 40)
        continue
    else:
        resistance = losses * power / (current ** 2)  # Desired resistance in Ohms based on power loss

    # Output cost for both Copper and Aluminum
    print(f"For {length} meters:")
    print(f"Diameter is {copper.diameter(length, resistance)}")
    print(f"Resistance per line is {(resistance*100/length)}")
    print(f"Current is {current}")
    print(f"Copper cost per meter: {copper.material_cost(length)/length:.2f} USD")
    print("-" * 40)
