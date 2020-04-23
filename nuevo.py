"""Walking Random
by Edwin Vasconez"""

import random as rm
import matplotlib.pyplot as plt
X = 0
Y = 0
MAX = 1000

def creaxey():
    ale1 = rm.randint(0,1)
    if ale1 == 1:
        return 1
    else:
        return -1
def creacaminate(X):
    x_pos = []
    for i in range(0, MAX + 1):
        X += creaxey()
        x_pos.append(X)
    return x_pos

def pasos():
    ini = 0
    lpasos = []
    for j in range(0, MAX + 1):
        ini += 1
        lpasos.append(ini)
    return lpasos

def creaensamble():
    listaensamble = []
    for j in range(0,100):
        listaensamble.append(creacaminate(X))

def main():
    lsteps = pasos()
    lcaminante = creacaminate(X)

    plt.plot(lsteps,lcaminante)
    plt.show()

main()

