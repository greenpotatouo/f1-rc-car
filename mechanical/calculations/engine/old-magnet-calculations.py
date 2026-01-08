import math

air_permeability = 4*math.pi*10**-7
core_permeability = 80*10**-3

permeability = air_permeability*core_permeability
number_turns_per_length = 157109 # turns per unit length

wire_gauge = 30 # awg
resistance = 169 # ohm per m
length = 1 # m
total_resistance = resistance * length
voltage = 12 # V

current = voltage/total_resistance
print(current)


coil_length = 0.05 # 50mm
coil_radius = 0.0175

magnet_radius = 0.0175
magnet_height = 0.005 # 5mm
magnet_volume = math.pi * magnet_radius ** 2 * magnet_height
remanent_flux_density = 1.2 # T
magnetic_moment = remanent_flux_density * magnet_volume / air_permeability
magnetism = magnetic_moment / magnet_volume
area = math.pi * magnet_radius ** 2 


def compute_magnetic_flux(z_position):
    B_term1 = z_position / (math.sqrt(coil_radius**2 + z_position**2))
    B_term2 = (z_position - coil_length) /  (math.sqrt(coil_radius**2 + (z_position - coil_length)**2))

    B_const = permeability*number_turns_per_length*current/2

    magnetic_flux = B_const * (B_term1 - B_term2)

    return magnetic_flux


def compute_force(z):
    B_1 = compute_magnetic_flux(z+coil_length)
    B_2 = compute_magnetic_flux(z)

    force = magnetism * area * (B_1 - B_2)

    return force

print(compute_force(-0.02)*10)

print(compute_force(-0.02)*0.05*10)
