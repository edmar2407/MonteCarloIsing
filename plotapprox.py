import matplotlib.pyplot as plt

f = open('cuadradosdeta=1.dat', 'r')
lsteps1 = []
leses1 = []
lemes1 = []
lbes1 = []

for line in f:
    linea1 = line.split(',')
    lsteps1.append(float(linea1[0]))
    leses1.append(float(linea1[1]))
    lemes1.append(float(linea1[2]))
    lbes1.append(float(linea1[3]))

f.close()

g = open('cuadradosdeta=0.1.dat', 'r')
lsteps2 = []
leses2 = []
lemes2 = []
lbes2 = []

for line in g:
    linea2 = line.split(',')
    lsteps2.append(float(linea2[0]))
    leses2.append(float(linea2[1]))
    lemes2.append(float(linea2[2]))
    lbes2.append(float(linea2[3]))

g.close()

fig, (ax1, ax2, ax3) = plt.subplots(3)
l1,=ax1.plot(lsteps1, leses1)
l2,=ax1.plot(lsteps2, leses2)
ax1.set(title='Minimos y Metropolis', ylabel='S/N')
ax2.plot(lsteps1, lbes1)
ax2.plot(lsteps2, lbes2)
ax2.set(ylabel='b')
ax3.plot(lsteps1, lemes1)
ax3.plot(lsteps2, lemes2)
ax3.set(xlabel='N', ylabel='m')

#plt.plot(lsteps, leses, label='S')

#plt.plot(lsteps, lemes, label='M')
#plt.plot(lsteps, lbes, label='B')
#plt.xscale('log', basex=10)
#plt.yscale('log', basey=10)
plt.legend([l1,l2],['B=1 y D=+/-1','B=1 y D=+/-0.1'])

plt.show()