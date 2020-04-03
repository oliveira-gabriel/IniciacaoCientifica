import argparse
import numpy as np

class Args:
    def __init__(self):
        self._parse_args()
        self._process_args_file()

        self.n_atoms = int(self.args_dict['n_atoms'])
        self.n_species = int(self.args_dict['n_species']) 
       
        self.specie_type_1 = self.args_dict['specie_type_1']
        self.specie_nat_1 = int(self.args_dict['specie_nat_1'])
        self.specie_type_2 = self.args_dict['specie_type_2']
        self.specie_nat_2 = int(self.args_dict['specie_nat_2'])

        self.mcs = int(self.args_dict['monte_carlo_steps'])
        #self.saving_mcs = int(self.args_dict['savemontecarlosteps'])
        self.particle_path = self.args_dict['geometry']
        self.temperature = np.float64(self.args_dict['temperature']) #Decimal
        self.log_file = self.args_dict['log_file']
        self.data_file = self.args_dict['data_file']
        self.reference_output = self.args_dict['reference_output']
    
    
    def _parse_args(self):
        parser = argparse.ArgumentParser()
    
        parser.add_argument('-f', action='store',
                            dest='args_file',
                            help='help...')
    
        results = parser.parse_args()
    
        #print(results.args_file)
    
        self.args_file = results.args_file

        self.args_file = 'args.txt'
    
    
    def _process_args_file(self):
        self.args_dict = {}
        with open(self.args_file, 'r') as file:
            for _, line in enumerate(file):
                line = line.strip()
                if not line.startswith('#') and line != '':
                    name_value = line.split()
                    if len(name_value) >= 2:
                        arg_name = name_value[0]
                        arg_value = name_value[1]
                        self.args_dict[arg_name.lower()] = arg_value

    def __str__(self):
        return str(self.args_dict)
    
    

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    