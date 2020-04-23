"""Walking Random
by Edwin Vasconez"""
import numpy as np
import matplotlib.pyplot as plt
X = 0
Y = 0
MAX = 200
for j in range(0, 3):
    x_pos = []
    y_pos = []
    for i in range(0, MAX + 1):
        plt.plot(x_pos, y_pos)
        X += (np.random.random() - 0.5)*2
        x_pos.append(X)
        Y += (np.random.random() - 0.5)*2
        y_pos.append(Y)
    plt.plot(x_pos, y_pos)
    X = 0
    Y = 0

plt.show()
