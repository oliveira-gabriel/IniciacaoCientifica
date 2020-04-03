import time
import utils
import numpy as np
from args import Args
#from files import Files

def main():
    time1 = time.time()
    print('Start:', time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime(time1)))
    args = Args()
    print(args)

    

    '''
    Ler arquivo args.reference_output
    searchLevel (achar abaixo e acima de Fermi)
    diferenca entre abaixo e acima (gap ref)
    '''
    below, above = utils.search_level(args.reference_output)
    ref_gap = abs(above - below)
    print(ref_gap)
   
    particle = utils.read_particle(args.particle_path)
    print('>'+str(particle).strip()+'<')

    print(args.specie_type_1)
    print(args.specie_nat_1)

    print(args.specie_type_2)
    print(args.specie_nat_2)

    #montar liga na fracao informada pelo usuario
    #Sorteio de posicoes
    from random import sample
    at_species = [args.specie_type_1]*args.n_atoms
    random_indices = sample(list(range(args.n_atoms)), args.specie_nat_2)
    for idx in random_indices:
        at_species[idx] = args.specie_type_2
    print(at_species)
    particle.at_species = at_species
    print('>'+str(particle).strip()+'<')


    template_file = open('input_template.in')
    content = template_file.read()
    template_file.close()
       
    content = content.replace('<#NAT#>', str(args.n_atoms))
    content = content.replace('<#NTYP#>', str(args.n_species))
    content = content.replace('<#PARTICLE#>', str(particle).strip())
    
    espresso_input_file = open('input.in', 'w')
    

    print(content)

    


    '''
    Colocar no template

    
    content = ""

    content = content.replace('<#NAT#>', args.n_atoms)
    content = content.replace('<#NTYP#>', args.n_species)
    content = content.replace('<#PARTICLE#>', conteudo_particula)
    #salvar arquivo -> new_content
    '''
 
    '''
    Chamar o espresso
    searchLevel (achar abaixo e acima de Fermi)
    diferenca entre abaixo e acima (gap liga)
    '''

    #diff_gap_step_1 = gap_ref - gap_lig

    #Fazer o swap de dois tipos diferentes
    #Colocar no template
    #Chamar o espresso (step 2)
    #searchLevel (achar abaixo e acima de Fermi)
    #diferenca entre abaixo e acima (gap liga)


    #diff_gap_step2 = gap_ref - gap_lig2

    #diff = diff_gap_step2 - diff_gap_step1
    #Se diff_gap_step2 é menor ou igual diff_gap_step1 aceita novo step2
    #senao  #exp(diff/kt)
            #sorteia em 0 e 1
            #Se aleatorio < exp aceita novo step2
            #senao rejeita step atual e volta para anterior
    #


    
if __name__ == '__main__':
    main()