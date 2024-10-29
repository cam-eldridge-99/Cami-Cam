# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math

def find_roof_area():
    building_width = int(input("How wide is your building in meters?\n"))
    building_length = int(input("How long is your building in meters?\n"))
    roof_angle= int(input("What is your roof angle in degrees?\n"))*(3.14/180)
    #math.cos(math.radians(roof_angle))
    roof_area = building_width * building_length / math.cos(roof_angle)
    print("\n Your available roof area is {:.2f} meters.".format(roof_area))
    return roof_area;
    
roof_area=find_roof_area()

class pvPanel():
    def __init__(self, pv_width, pv_height, pv_power):
        self.pv_width = pv_width
        self.pv_height = pv_height
        self.pv_power = pv_power
        
def pv_area(self):
    pv_area = (self.pv_width/1000) * (self.pv_height/1000)
    return pv_area;

ourPanel = pvPanel( 1690, 1046, 400)

panelArea = pv_area(ourPanel)

numPanels = math.floor(roof_area / panelArea)

print("Each panel is {:.2f} square meters.\n".format(panelArea))

print("The roof will fit {} panels.".format(numPanels))
