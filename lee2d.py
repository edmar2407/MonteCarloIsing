import matplotlib.pyplot as plt

f = open('tem2data2.txt', 'r')
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

g = open('tem2data2.3.txt', 'r')
for line in g:
    linea2 = line.split(',')
    lseda.append(float(linea2[1]))
g.close()

m = open('tem2data3.txt','r')
for line in m:
	linea3 = line.split(',')
	l.append(float(linea3[1]))
m.close()

plt.plot(lpris, lprida, label='T=2')
plt.plot(lpris, lseda, label='T=2.3')
plt.plot(lpris, l,'r',label='T=3')
plt.xscale('log', basex=10)
plt.legend()

plt.show()