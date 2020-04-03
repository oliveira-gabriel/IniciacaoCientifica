import numpy as np
from const import X, Y, Z

class Particle:
    def __init__(self, name=None, number_of_atoms=0, at_species=None, atoms=None):
        self.name = name
        self.number_of_atoms = number_of_atoms
        self.at_species = at_species
        self.atoms = atoms
        #self.atoms_cn = np.zeros(number_of_atoms,  dtype=np.float64) 
        #self.atoms_gcn = np.zeros(number_of_atoms,  dtype=np.float64) 
           
    def __str__(self):
        str_ = ''
        for i, atm in enumerate(self.atoms):
            str_ += self.at_species[i] + ' '
            str_ += str(atm[X])+' '
            str_ += str(atm[Y])+' '
            str_ += str(atm[Z])+' '
            #str_ += str(self.atoms_cn[i])+'\t'
            #str_ += str(self.atoms_gcn[i])
            str_ += '\n'
        return str_