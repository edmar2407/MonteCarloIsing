import matplotlib.pyplot as plt
import numpy as np
MAX = 10**4
BETA = 1
def creaxey():
    ale1 = np.random.randint(2)
    if ale1 == 1:
        return 1
    else:
        return -1

def creardatos(nombre):
	listadatax = []
	listadatay = []
	f = open(nombre,'r')
	for line in f:
		data = line.split(' ')
		listadatax.append(float(data[0]))
		listadatay.append(float(data[1]))
	f.close()
	return listadatax, listadatay
	#plt.plot(listadatax, listadatay)
	#plt.show()

def calculaym(m, b, lx, j):
	y_m = m*lx[j] + b
	return y_m

def aleeninter():
	numale = np.random.random()
	numafi = numale*creaxey()
	return numafi/10

def creardat(l1, l2, l3, l4):
	f = open('cuadradosdeta=0.1.dat','w')
	for i in range(len(l1)):
		f.write(str(l1[i])+','+str(l2[i])+','+str(l3[i])+','+str(l4[i])+'\n')
	f.close()

def main():
	file = 'datos.dat'
	ldatosx, ldatosy = creardatos(file)
	m = 5
	b = 8
	lemes = []
	leses = []
	lbes = []
	lsteps = []
	for i in range(0, MAX):
		aleatorio1 = aleeninter()
		aleatorio2 = aleeninter()
		m += aleatorio1
		b += aleatorio2
		#ym = calculaym(m, b, ldatosx, )
		dsini = 0
		dsfi = 0
		for j in range(len(ldatosy)):
			ymini = calculaym(m - aleatorio1, b - aleatorio2, ldatosx, j)
			ymfi = calculaym(m, b, ldatosx, j)
			dsini += (ldatosy[j] - ymini)**2
			dsfi += (ldatosy[j] - ymfi)**2
			s = dsfi - dsini


		if s < 0:
			m = m
			b = b
		else:
			aleat = np.random.random()
			if np.exp(-BETA*s) > aleat:
				m = m
				b = b
			else:
				m -= aleatorio1
				b -= aleatorio2
		#print(m)
		if i%100 == 0:
			leses.append(s/len(ldatosx))
			lemes.append(m)
			lbes.append(b)
			lsteps.append(i)
	creardat(lsteps,leses,lemes,lbes)



main()