import math
import numpy as np

def x():
    return 1.0

def xi():
    return [-1.0, 0, 2.0]

def yi():
    return [4.0, 1.0, -1.0]

def lagrange():
    count = 0

    n  = len(xi())
    
    P = 0.0
    for k in range(n):
        P = P + yi()[k] * calc_lagrange(k, x(), xi())

        #Iteração
        print('Iteração '+ str(count))
        print('--------------------------------') 
        print(P)
        print()

        count = count + 1


def calc_lagrange(k, x, xi):
    l_nk = 1.0
    n   = len(xi)
    for i in range(n):
        if (i != k):
            l_nk = l_nk * ( (x - xi[i]) / (xi[k] - xi[i]) )
    
    return l_nk

def newton():
    count = 0

    matriz = []

    vetor = xi().copy()
    matriz = yi().copy()
    
    for i in range(len(vetor)):
        matriz[i] = yi().copy()

    for i in range(1, len(vetor)):
        for j in range(i, len(vetor)):
            matriz[j][i] = (matriz[i-1][j] - matriz[j-1][i-1]) / (vetor[j] - vetor[j-i])

    aprx = 0
    P = 0.0
    for i in range(len(vetor)):
        P = matriz[i][i]

        for j in range(1, i+1):
            P = P * (x() - vetor[j - 1])
        aprx = aprx + P

        #Iteração
        print('Iteração '+ str(count))
        print('--------------------------------') 
        print(aprx)
        print()

        count = count + 1
