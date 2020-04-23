import numpy as np
import matplotlib.pyplot as plt

MAX = 1000000
BETA = 3
SPIN = 1000

def creaxey():
    ale1 = np.random.randint(2)
    if ale1 == 1:
        return 1
    else:
        return -1

def creacaminate():
    x_pos = np.zeros(SPIN)
    for i in range(0, SPIN):
        x_pos[i] = creaxey()
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
        if i == SPIN-1:
            ener -= lista[i]*lista[0]
        else:
            ener -= lista[i]*lista[i+1]
    return ener


def deltaenergy(lista,indi):
    lon = len(lista)
    if indi == 0:
        delenergy = 2*lista[indi]*(lista[indi+1]+lista[lon-1])
    elif indi == lon-1:
        delenergy = 2*lista[indi]*(lista[indi-1]+lista[0])
    else:
        delenergy = 2*lista[indi]*(lista[indi+1]+lista[indi-1])
    return delenergy

def main():
    lsteps = pasos()
    caminante = creacaminate()
    energia = []
  
    for i in range(0, MAX-1):
        index = np.random.randint(SPIN)
        delindex = deltaenergy(caminante, index)
        if delindex < 0:
            caminante[index] *= -1
        else:
            aleat = np.random.random()
            if np.exp(-BETA*delindex) > aleat:
                caminante[index] *= -1
        if i%1000==0:
            energia.append(energy(caminante)/MAX)



    energiatotal = energia
    plt.semilogx(lsteps[:-1], energiatotal[:-1])
    plt.show()
main()
