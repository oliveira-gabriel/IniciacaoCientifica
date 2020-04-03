import numpy as np

X = 0
Y = 1
Z = 2
CN = 3
GCN = 4

# :param min_dst: distancia minina considera para um atomo ser um vizinho
MIN_DIST = np.float64(2.912561) #Usuario vai informar na entrada
# :param cn_max: numero maximo de coordenacao de um atomo em uma estrutura fcc
MAX_CN = np.float64(12)