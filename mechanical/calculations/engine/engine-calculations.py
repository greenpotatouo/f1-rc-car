import math
import json

with open('wire-properties.json', 'r') as f:
    wire_properties = json.load(f)

gauge = '26'
OD = 0.032 # m
ID = 0.025 # m
wire_diameter = wire_properties[gauge]['diameter']/1000 # m
resistance_per_km = wire_properties[gauge]['resistance'] 

voltage = 30 # V
coil_diameter = OD

magnet_diameter = 0.02
magnet_length = 0.01
remanent_flux_density = 1.2
crankshaft_radius = 0.01
number_pistons = 10

coil_length = crankshaft_radius*4 # m

coil_thickness = (OD-ID)/2
number_turns_per_layer = coil_thickness/wire_diameter


number_turns_per_m = number_turns_per_layer*(1/wire_diameter)
print(f'{round(number_turns_per_m)}turns/m')


air_permeability = 4*math.pi*10**-7
coil_radius = coil_diameter/2
magnet_radius = magnet_diameter/2
magnet_volume = math.pi * magnet_radius ** 2 * magnet_length
magnetic_moment = remanent_flux_density * magnet_volume / air_permeability
magnetism = magnetic_moment / magnet_volume
area = math.pi * magnet_radius ** 2


length_per_layer = 0

for i in range(1, round(number_turns_per_layer+1)):
    length_per_layer += math.pi * (wire_diameter*i + ID)

number_layers = coil_length/wire_diameter
total_length = length_per_layer * number_layers
total_length_km = total_length/1e3
print(f'{round(total_length, 2)}m')

total_resistance = total_length_km * resistance_per_km
print(f'{round(total_resistance, 2)}Ω')

current = voltage / total_resistance
print(f'{round(current, 2)}A')


def compute_magnetic_flux(z_position):
    z1 = z_position - coil_length
    z2 = z_position + coil_length

    B_term1 = z2 / math.sqrt(coil_radius**2 + z2**2)
    B_term2 = z1 / math.sqrt(coil_radius**2 + z1**2)

    B_const = air_permeability*number_turns_per_m*current/2

    magnetic_flux = B_const * (B_term1 - B_term2)

    return magnetic_flux


def compute_force(z):
    B_1 = compute_magnetic_flux(z+magnet_length/2)
    B_2 = compute_magnetic_flux(z-magnet_length/2)

    force = magnetism * area * (B_1 - B_2)

    return force


print(compute_force(-coil_length)*crankshaft_radius*number_pistons)
