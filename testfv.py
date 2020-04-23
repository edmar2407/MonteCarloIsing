"""
Test for random numbers
by Edwin Marcelo Vasconez Lopez
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['lines.linewidth'] = 1


def test1y2(lis1, lis2, lis3):
    """Test1: Plot sequence number vs Random Number"""
    plt.subplot(1, 2, 1)
    plt.plot(lis1, lis2)
    plt.title('TEST 1')
    plt.xlabel('Sequence Number')
    plt.ylabel('Ramdom Number r')
    # Test2: Plot r_i vs r_i+1
    plt.subplot(1, 2, 2)
    plt.plot(lis2, lis3, '+', color='r')
    plt.title('TEST 2')
    plt.xlabel('r_i')
    plt.ylabel('r_i+1')
    plt.show()


def test3(lis1):
    """Test 3:
    Test of uniformity evaluates the kth moment of distribution
    In my case k = 1
    Equation [5.10] book"""
    suma = 0
    index = 0
    k = 1
    for num in lis1:
        suma += num
        index += 1
    total = suma/index
    total1 = (1/(k+1)) + (1/(index**(1/2)))

    print("TEST 3")
    print("Moment of distribution problem:"+'\t\t\t', total)
    print("Moment of distribution approximation:"+'\t\t', total1)


def test4(lis1, lis2):
    """Test 4:
    Near-neighbor correlation"""
    suma4 = 0
    index = 0
    for i in range(len(lis1)):
        suma4 += lis1[i]*lis2[i]
        index += 1
    total4 = suma4/index

    print("TEST 4")
    print("Near-neighboor correlation problem:"+'\t\t', total4)
    print("Near-neighboor correlation approximation:"+'\t', 1/4)


def main():
    """Main Function"""
    listaindex = []
    lista = []
    listanew = []
    i = 0
    file = open('Aleatorios.txt', 'r')
    for linea in file:
        lista.append(float(linea))
        listaindex.append(i)
        listanew.append(0)
        i += 1
    file.close()

    for i in range(len(lista)-1):
        listanew[i] = lista[i+1]

    test3(lista)
    test4(lista, listanew)
    test1y2(listaindex, lista, listanew)

main()
