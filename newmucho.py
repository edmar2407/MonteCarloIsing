import numpy as np
import random as rm
import matplotlib.pyplot as plt

MAX = 1000000
NUMC = 1000

def creaxey():
    ale1 = rm.randint(0,1)
    if ale1 == 1:
        return 1
    else:
        return -1
def creacaminate():
    X = 0
    x_pos = np.zeros(MAX)
    for i in range(0, MAX):
        X += creaxey()
        x_pos[i] = X
    return x_pos

def pasos():
    ini = 0
    lpasos = np.zeros(MAX)
    for j in range(0, MAX):
        ini += 1
        lpasos[j] = ini
    return lpasos

def creaensamble():
    lensamble = np.zeros(NUMC, dtype=object)
    for j in range(0, NUMC):
        lensamble[j] = creacaminate()
    return lensamble


def main():
    lsteps = pasos()
    ltodos = creaensamble()
    promedio = np.sum(ltodos,axis=0)
    promedio2 = np.sum(ltodos**2,axis=0)
    promedio2 = promedio2/MAX
    promedio = promedio/MAX
    final = np.sqrt(promedio2 - promedio*promedio)

    plt.loglog(lsteps,final)
    plt.show()

main()