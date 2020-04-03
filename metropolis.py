import numpy as np
import random
import csv
import os



#Recebera uma opcao de escolha , para mudar ou nao 
def swapAt(op):
    #A deltaUm eh o melhor 
    if op is 1:
        with open('input1.in','r') as inf:
            #incsv = csv.reader(inf) #print(incsv) 
            inputIn = [line.split() for line in inf]  
        
        compara = ['ATOMIC_POSITIONS','{angstrom}']

        with open('input1.in','w', newline = '') as inf:
            outIn = csv.writer(inf, skipinitialspace=True, delimiter = ' ')

            for x in range(len(inputIn)):
                if x != []:
                    outIn.writerow(inputIn[x])
                #Inicio da troca , o numero da random tera que ser mudado de acordo com o numero
                #de atomos da particula , caso troque a particula 
                if inputIn[x] == compara:

                    al1 = random.randrange(1,5)
                    x1 = random.randrange(1,5)
                    aux = inputIn[x+x1+1][0]

                    while inputIn[x + al1][0] == inputIn[x+x1][0] :
                        al1 = random.randrange(4)+1

                    #Troca os atomos de lugar 
                    inputIn[x+al1][0],inputIn[x+x1][0]= inputIn[x+x1][0] ,inputIn[x+al1][0]
                    print(inputIn[x+al1][0])
                    print(inputIn[x+x1][0])
    #se o segundo eh melhor
    elif op is 2:
        with open('input2.in','r') as inf:
            incsv = csv.reader(inf) #print(incsv) 
            inputIn = [line.split() for line in inf]  

       
        compara = ['ATOMIC_POSITIONS','{angstrom}']

        

        with open('input1.in','w', newline = '') as inf:
            outIn = csv.writer(inf, skipinitialspace=True, delimiter = ' ')

            for x in range(len(inputIn)):
                if x != []:
                    outIn.writerow(inputIn[x])
                #Inicio da troca , o numero da random tera que ser mudado de acordo com o numero
                #de atomos da particula , caso troque a particula 
                if inputIn[x] == compara:

                    al1 = random.randrange(1,5)
                    x1 = random.randrange(1,5)
                    aux = inputIn[x+x1+1][0]

                    while inputIn[x + al1][0] == inputIn[x+x1][0] :
                        al1 = random.randrange(4)+1

                    #Troca os atomos de lugar 
                    inputIn[x+al1][0],inputIn[x+x1][0]= inputIn[x+x1][0] ,inputIn[x+al1][0]


def searchLevel():
    # Lendo o Arquivo 
    with open('output.out','r') as inf:
        #inf.readline()
        incsv = csv.reader(inf)
        leitura =[line.split() for line in inf] 

    #print(leitura)


    #Criando um lista a partir do arquivo
    output = []

    for x in range(len(leitura)):
        if leitura[x] != output: 
            output.append(leitura[x]) 
            #print(output[x])


    # Identificando o bloco e a Energia de Fermi           
    for i in range (len(output)):
        for j in range(len(output[i])):
            if output[i][j]== 'Fermi':
                print( output[i])  
                blockStart = i - 37
                blockEnd = i - 2
                energyFermi = float(output[i][j+3])


    print(blockStart)
    print(blockEnd)
    print(blockEnd - blockStart)


    #Identificando o proximo nivel para calcular a diferenca 
    while blockStart != blockEnd:
        for coll in range(len(output[blockStart])):
            #print(output[blockStart][coll])
            if float(output[blockStart][coll]) < float(energyFermi):

                level = float(output[blockStart][coll])



        blockStart+= 1


    return level 

    
                    
def teste_searchLevel():
    with open('output.out','r') as file:
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
#-4.4896 

print(teste_searchLevel())
