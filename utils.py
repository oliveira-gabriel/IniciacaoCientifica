import numpy as np
from const import X, Y, Z
from particle import Particle

def read_particle(path) -> Particle:
    with open(path) as file:
        number_of_atoms = int(next(file))
        name = next(file)
        atoms = np.empty(shape=(number_of_atoms, 3), dtype=np.float64)

        at_species = []
        print(at_species)

        for index, line in enumerate(file):
            list_line = line.split()
            at_species.append(list_line[0])
            atoms[index][X] = list_line[1]
            atoms[index][Y] = list_line[2]
            atoms[index][Z] = list_line[3]
    return Particle (name=name, number_of_atoms=number_of_atoms, at_species=at_species, atoms=atoms)
    
def search_level(file):
    with open(file,'r') as file:
        content = file.read()

    start = content.index('End of self-consistent calculation')
    end = content.index('the Fermi energy is')
    fermi = float(content[end+23:end+30])

    line_list = content[start: end].split('\n')[4:-2]

    above = None
    for line in line_list:
        values = line.split()
        for value in values:
            f_value = float(value) 
            if f_value < fermi:
                below = float(value)

            if above is None and f_value > fermi:
                above = float(value)

    return below, above





    

    


 


  

def get_boltzmann_weight(old_target_diff, new_target_diff, temperature, num_atoms):
    # Coracao do Monte de Carlo: 'Peso de boltzmann'
    difference = abs(new_target_diff - old_target_diff)
    ab = -1 * (difference) / (temperature / num_atoms)
    return np.exp(ab)  # Entre 0 e 1 
    







    