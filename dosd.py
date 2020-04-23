import numpy as np
import random as rm
import matplotlib.pyplot as plt

MAX = 100000

def creaxey():
    ale1 = rm.randint(0,1)
    if ale1 == 1:
        return 1
    else:
        return -1

def creacaminate():
    X = 0
    Y = 0
    x_pos = np.zeros(MAX)
    y_pos = np.zeros(MAX)
    for i in range(0, MAX):
        X += creaxey()
        x_pos[i] = X
        Y += creaxey()
        y_pos[i] = Y
    return x_pos, y_pos

def pasos():
    ini = 0
    lpasos = np.zeros(MAX)
    for j in range(0, MAX):
    	ini += 1
    	lpasos[j] = ini
    return lpasos

def main():
    lsteps = pasos()
    xarray, yarray = creacaminate()
    prox = 0
    lprox = np.zeros(MAX)
    for i in range(len(xarray)):
        prox += np.sqrt(xarray[i]*xarray[i] + yarray[i]*yarray[i])
        lprox[i] = prox

    #plt.plot(xarray, yarray)

    plt.loglog(lsteps,lprox)
    plt.show()

main()