# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:36:29 2024

@author: 2024
"""

import matplotlib.pyplot as plt  # Correct import for matplotlib

E = 1.0  # Voltage of the source (V)
Rs = 0.1  # Source resistance (Ohms)

# Create empty lists to store load (resistance), power output, and efficiency
loads = []
power_out = []
efficiency = []

# Tolerance for comparing floating-point numbers
tolerance = 1e-5

for i in range(0, 201):
    Rl = i / 100  # Load resistance (0 to 2 Ohms in steps of 0.01)
    I = E / (Rs + Rl)  # Current calculation (Ohm's Law: I = V / R)
    p_in = I * E  # Input power (P_in = I * V)
    p_out = I**2 * Rl  # Output power (P_out = I^2 * Rl)

    # Store the load and corresponding output power
    loads.append(Rl)
    power_out.append(p_out)

    # Efficiency calculation (P_out / P_in)
    if p_in == 0:
        efficiency.append(0)
    else:
        efficiency.append(p_out / p_in)
    
    # Print power output when it is close to 1 W (within a tolerance)
    if abs(1 - p_out) < 0.01:
        print(f"At {Rl} Ohms, power out is {p_out} watts")

    # Print efficiency near 0.95 and corresponding power
    if abs(0.95 - (I * Rl / E)) < tolerance:
        print(f"Efficiency is {p_out / p_in} when load is {Rl} ohms")
        print(f"Power at {Rl} ohms is {p_out} watts")

# Now show max Power out
max_power = max(power_out)
max_power_index = power_out.index(max_power)
max_power_load = loads[max_power_index]
print(f"Maximum power is {max_power} watts at {max_power_load} ohms")

# Create a figure and axis
fig, ax1 = plt.subplots()

# Plot power output on the left-hand y-axis
ax1.plot(loads, power_out, label="Power Output", color='b')
ax1.set_xlabel("Load Resistance (Ohms)")
ax1.set_ylabel("Power Output (W)")
ax1.tick_params(axis='y')

# Mark the maximum power point on the plot
ax1.scatter(max_power_load, max_power, color='r', label=f"Max Power ({max_power:.2f} W)")

# Create a second y-axis for efficiency
ax2 = ax1.twinx()
ax2.plot(loads, efficiency, label="Efficiency", color='g')
ax2.set_ylabel("Efficiency")
ax2.tick_params(axis='y')

# Adding titles and labels
plt.title("Power Output and Efficiency vs. Load Resistance")
ax1.grid(True)

# Now we explicitly add both legends
ax1.legend(loc='lower right')  # Legend for power
ax2.legend(loc='lower left')  # Legend for efficiency

# Show the plot with legends for both axes
fig.tight_layout()
plt.show()
