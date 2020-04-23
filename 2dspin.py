import numpy as np
import matplotlib.pyplot as plt
T = 3
KB = 1
MAX = 10000
BETA = 1/(KB*T)
SPIN = 100

def creaxey():
    ale1 = np.random.randint(2)
    if ale1 == 1:
        return 1
    else:
        return -1

def creacaminate():
    x_pos = np.zeros((SPIN, SPIN))
    for i in range(0, SPIN):
        for j in range(0, SPIN):
            x_pos[i][j] = creaxey()
    return x_pos

def pasos():
    ini = 0
    lpasos = []
    for j in range(0, MAX):
        if j%1000 == 0:
            lpasos.append(ini)
        ini += 1
    return lpasos

def energy(lista):
    ener = 0
    for i in range(0, SPIN):
        for j in range(0, SPIN):
            ener -= lista[i][j]
    return ener


def deltaenergy(lista,indix, indiy):
    delenergy = 2*lista[indix][indiy]*(lista[indix][indiy+1] + lista[indix][indiy-1] + lista[indix+1][indiy] + lista[indix-1][indiy])
    return delenergy

def creartxt(lista1, lista2):
    f = open('tem2data'+str(T)+'.txt','w')
    for i in range(len(lista1)):
        f.write(str(lista1[i])+','+str(lista2[i])+'\n')
    f.close()



def main():
    lsteps = pasos()
    caminante = creacaminate()
    energia = [0]
  
    for i in range(0, MAX):
        index_x = np.random.randint(0,SPIN-1)
        index_y = np.random.randint(0,SPIN-1)
        delindex = deltaenergy(caminante, index_x, index_y)
        if delindex < 0:
            caminante[index_x][index_y] *= -1
        else:
            aleat = np.random.random()
            if np.exp(-BETA*delindex) > aleat:
                caminante[index_x][index_y] *= -1
        if i%1000==0:
            energia.append(energy(caminante)/(SPIN*SPIN))
    creartxt(lsteps[:-1], energia[:-1])
main()
