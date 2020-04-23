import matplotlib.pyplot as plt

f = open('data3.txt', 'r')
lpris = []
lprida = []
lseda = []
l = []
lcua = []
for line in f:
    linea1 = line.split(',')
    lpris.append(float(linea1[0]))
    lprida.append(float(linea1[1]))
f.close()

g = open('data0.1.txt', 'r')
for line in g:
    linea2 = line.split(',')
    lseda.append(float(linea2[1]))
g.close()

m = open('data1.txt','r')
for line in m:
	linea3 = line.split(',')
	l.append(float(linea3[1]))
m.close()

h = open('data1.75.txt', 'r')
for line in h:
	linea4 = line.split(',')
	lcua.append(float(linea4[1]))
h.close()

plt.semilogx(lpris, lprida, label='beta=3')
plt.semilogx(lpris, lseda, label='beta=0.1')
plt.semilogx(lpris, l,'r',label='beta=1')
plt.semilogx(lpris, lcua, label='beta=1.75')
plt.legend()

plt.show()