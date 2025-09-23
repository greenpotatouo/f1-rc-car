import json
import math

with open('wire-properties.json', 'r') as f:
    wire_properties = json.load(f)

gauge = '30'
OD = 32 # mm
ID = 22 # mm
height = 40 # mm
coil_thickness = (OD-ID)/2

voltage = 15 # V

wire_diameter = wire_properties[gauge]['diameter'] # mm
resistance_per_km = wire_properties[gauge]['resistance'] 

number_turns_per_layer = coil_thickness/wire_diameter
print(number_turns_per_layer)
print(f'{round(number_turns_per_layer*(1000/wire_diameter))}turns/m')

length_per_layer = 0

for i in range(1, math.ceil(number_turns_per_layer+1)):
    length_per_layer += math.pi * (wire_diameter*i + ID)

number_layers = height/wire_diameter

total_length = length_per_layer * number_layers

print(f'{round(total_length/1000, 2)}m')

total_length_km = total_length/1e6

total_resistance = total_length_km * resistance_per_km

print(f'{round(total_resistance, 2)}Ω')


# current_target = 1 # A

# required_voltage = current_target * total_resistance

# print(f'{round(required_voltage, 2)}V')

current = voltage / total_resistance

print(f'{round(current, 2)}A')

