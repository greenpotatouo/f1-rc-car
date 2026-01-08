import math

air_permeability = 4*math.pi*10**-7

number_turns_per_length = 77500 # turns per m

wire_gauge = 30 # awg
resistance = 169 # ohm per m
wire_length = 1 # m
total_resistance = resistance * wire_length
voltage = 12 # V

current = voltage/total_resistance
current = 0.18

coil_length = 0.40
coil_radius = 0.016

magnet_diameter = 0.02
magnet_radius = magnet_diameter / 2
magnet_length = 0.01
magnet_volume = math.pi * magnet_radius ** 2 * magnet_length
remanent_flux_density = 1.2 # T
magnetic_moment = remanent_flux_density * magnet_volume / air_permeability

magnetism = magnetic_moment / magnet_volume
area = math.pi * magnet_radius ** 2 


def compute_magnetic_flux(z_position):
    z1 = z_position - coil_length
    z2 = z_position + coil_length

    B_term1 = z2 / math.sqrt(coil_radius**2 + z2**2)
    B_term2 = z1 / math.sqrt(coil_radius**2 + z1**2)

    B_const = air_permeability*number_turns_per_length*current/2

    magnetic_flux = B_const * (B_term1 - B_term2)

    return magnetic_flux


def compute_force(z):
    B_1 = compute_magnetic_flux(z+magnet_length/2)
    B_2 = compute_magnetic_flux(z-magnet_length/2)

    force = magnetism * area * (B_1 - B_2)
    print(magnetism)
    return force


# print(compute_force(-0.03)*10)
# print(compute_magnetic_flux(0.04)*10)
print(compute_force(-coil_length)*0.01*10)
