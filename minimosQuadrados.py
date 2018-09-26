import math
import numpy as np

def linear():
    #Lendo arquivo com a matriz
    nome_arq = "tabelamento.txt"
    arq = open(nome_arq, "r")
    
    #Atribui a Tabelamento a Matriz
    matriz = arquivo_para_matriz(arq.readlines())

    #Número de linhas da matriz (quantidade de pontos)
    n = len(matriz)

    somaX = 0
    somaY = 0
    somaXY = 0
    somaXX = 0
    for i in range(n):
        somaX += matriz[i][0]
        somaY += matriz[i][1]
        somaXY += matriz[i][0]*matriz[i][1]
        somaXX += matriz[i][0]*matriz[i][0]

    a = (n*somaXY - somaX*somaY)/(n*somaXX - (somaX ** 2))
    b = (somaX*somaXY - somaY*somaXX)/((somaX ** 2) - n*somaXX)
    
    print('--------------------------------')
    print("Valor de a: "+str(a))
    print("Valor de b: "+str(b))
    print('--------------------------------')

def logaritmo():
    #Lendo arquivo com a matriz
    nome_arq = "tabelamento.txt"
    arq = open(nome_arq, "r")
    
    #Atribui a Tabelamento a Matriz
    matriz = arquivo_para_matriz(arq.readlines())

    #Número de linhas da matriz (quantidade de pontos)
    n = len(matriz)

    somaX = 0
    somaY = 0
    somaXY = 0
    somaXX = 0
    for i in range(n):
        somaX += math.log(matriz[i][0])
        somaY += matriz[i][1]
        somaXY += math.log(matriz[i][0])*matriz[i][1]
        somaXX += math.log(matriz[i][0])*math.log(matriz[i][0])

    a = (n*somaXY - somaX*somaY)/(n*somaXX - (somaX ** 2))
    b = (somaX*somaXY - somaY*somaXX)/((somaX ** 2) - n*somaXX)
    
    print('--------------------------------')
    print("Valor de a: "+str(a))
    print("Valor de b: "+str(b))
    print('--------------------------------')

def exponencial():
    #Lendo arquivo com a matriz
    nome_arq = "tabelamento.txt"
    arq = open(nome_arq, "r")
    
    #Atribui a Tabelamento a Matriz
    matriz = arquivo_para_matriz(arq.readlines())

    #Número de linhas da matriz (quantidade de pontos)
    n = len(matriz)

    somaX = 0
    somaY = 0
    somaXY = 0
    somaXX = 0
    for i in range(n):
        somaX += matriz[i][0]
        somaY += math.log(matriz[i][1])
        somaXY += matriz[i][0]*math.log(matriz[i][1])
        somaXX += matriz[i][0]*matriz[i][0]

    a = (n*somaXY - somaX*somaY)/(n*somaXX - (somaX ** 2))
    b = (somaX*somaXY - somaY*somaXX)/((somaX ** 2) - n*somaXX)
    b = math.exp(b)
    
    print('--------------------------------')
    print("Valor de a: "+str(a))
    print("Valor de b: "+str(b))
    print('--------------------------------')

def potencia():
    #Lendo arquivo com a matriz
    nome_arq = "tabelamento.txt"
    arq = open(nome_arq, "r")
    
    #Atribui a Tabelamento a Matriz
    matriz = arquivo_para_matriz(arq.readlines())

    #Número de linhas da matriz (quantidade de pontos)
    n = len(matriz)

    somaX = 0
    somaY = 0
    somaXY = 0
    somaXX = 0
    for i in range(n):
        somaX += math.log(matriz[i][0])
        somaY += math.log(matriz[i][1])
        somaXY += math.log(matriz[i][0])*math.log(matriz[i][1])
        somaXX += math.log(matriz[i][0])*math.log(matriz[i][0])

    a = (n*somaXY - somaX*somaY)/(n*somaXX - (somaX ** 2))
    b = (somaX*somaXY - somaY*somaXX)/((somaX ** 2) - n*somaXX)
    b = math.exp(b)
    
    print('--------------------------------')
    print("Valor de a: "+str(a))
    print("Valor de b: "+str(b))
    print('--------------------------------')
    

#METODOS AUXILIARES ======================================================================
def arquivo_para_matriz(arq):
    return [[float(x) for x in line.split()] for line in arq]