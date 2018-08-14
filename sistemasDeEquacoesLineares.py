import math
import numpy as np

def gauss():
    count = 0

    #Lendo arquivo com a matriz
    nome_arq = "matriz_aumentada.txt"
    arq = open(nome_arq, "r")
    
    #Atribui a Matriz Aumentada a variável matrizA
    matrizA = arquivo_para_matriz(arq.readlines())
    #Cria o vetor vazio B
    vetorB = []

    #Número de linhas da matriz dos cofatores
    lin = len(matrizA)
    
    #Divide a matriz aumentada em duas
    for i in range(lin):
        vetorB.append(matrizA[i][lin])
        matrizA[i].pop(lin)
    
    #Número de colunas da matriz dos cofatores
    col = len(matrizA[0])

    #Verifica se a matriz dos cofatores é quadrada
    if (lin != col):
        print("Matriz [", col, "X", lin, "] não é quadrada")
        print(np.matrix(matrizA))
    else:
        pivo = 0 
        mL = 0

        #Matriz inicial
        print('Iteração '+ str(count))
        print('--------------------------------')
        print('Matriz dos coeficientes')
        print(np.matrix(matrizA))
        print('Vetor dos resultados')
        print(np.matrix(vetorB))
        print()

        for k in range(lin - 1):
            pivo = matrizA[k][k]
            for i in range(k + 1, lin):
                mL = (matrizA[i][k])/pivo
                for j in range(col):
                    matrizA[i][j] = round(matrizA[i][j] - (mL * matrizA[k][j]), const_aprox())
                vetorB[i] = round(vetorB[i] - (mL * vetorB[i - 1]), const_aprox())

            count = count + 1

            #Iteração
            print('Iteração '+ str(count))
            print('--------------------------------') 
            print('Matriz dos coeficientes')
            print(np.matrix(matrizA))
            print('Vetor dos resultados')
            print(np.matrix(vetorB))
            print()


def lu():
    count = 0

    #Lendo arquivo com a matriz
    nome_arq = "matriz_aumentada.txt"
    arq = open(nome_arq, "r")
    
    #Atribui a Matriz Aumentada a variável matrizA
    matrizU = arquivo_para_matriz(arq.readlines())
    #Cria o vetor vazio B
    vetorB = []
    matrizL = []

    #Número de linhas da matriz dos cofatores
    lin = len(matrizU)

    #Divide a matriz aumentada em duas
    for i in range(lin):
        vetorB.append(matrizU[i][lin])
        matrizU[i].pop(lin)
    
    #Popula matriz L
    for i in range(lin):
        matrizL.append([])
        for j in range(lin):
            if(i == j):
                matrizL[i].append(1)
            else:
                matrizL[i].append(0)
    
    #Número de colunas da matriz dos cofatores
    col = len(matrizU[0])

    #Verifica se a matriz dos cofatores é quadrada
    if (lin != col):
        print("Matriz [", col, "X", lin, "] não é quadrada")
        print(np.matrix(matrizU))
    else:
        pivo = 0 
        mL = 0

        #Matriz inicial
        print('Iteração '+ str(count))
        print('--------------------------------') 
        print('Matriz L')
        print(np.matrix(matrizL))
        print()
        print('Matriz U')
        print(np.matrix(matrizU))
        print('Vetor dos resultados')
        print(np.matrix(vetorB))
        print()

        for k in range(lin - 1):
            pivo = matrizU[k][k]
            for i in range(k + 1, lin):
                mL = (matrizU[i][k])/pivo
                for j in range(col):
                    matrizU[i][j] = round(matrizU[i][j] - (mL * matrizU[k][j]), const_aprox())
                    if(matrizU[i][j] == 0 and i > j and matrizL[i][j  ] == 0):
                        matrizL[i][j] = round(mL, const_aprox())

            count = count + 1

            #Iteração
            print('Iteração '+ str(count))
            print('--------------------------------')
            print('Matriz L')
            print(np.matrix(matrizL))
            print()
            print('Matriz U')
            print(np.matrix(matrizU))
            print('Vetor dos resultados')
            print(np.matrix(vetorB))
            print()
    

def jacobi():
    count = 0

    #Lendo arquivo com a matriz
    nome_arq = "matriz_aumentada.txt"
    arq = open(nome_arq, "r")
    
    #Atribui a Matriz Aumentada a variável matrizA
    matrizA = arquivo_para_matriz(arq.readlines())
    #Cria o vetor vazio B
    vetorB = []

    #Número de linhas da matriz dos cofatores
    lin = len(matrizA)
    
    #Divide a matriz aumentada em duas
    for i in range(lin):
        vetorB.append(matrizA[i][lin])
        matrizA[i].pop(lin)
    
    #Número de colunas da matriz dos cofatores
    col = len(matrizA[0])

    #Verifica se a matriz dos cofatores é quadrada
    if (lin != col):
        print("Matriz [", col, "X", lin, "] não é quadrada")
        print(np.matrix(matrizA))
    else:
        criterio_linha = 0
        for i in range(lin):
            linha = 0
            for j in range(col):
                if(i == j):
                    maior = matrizA[i][j]
                else:
                    linha += matrizA[i][j]
            if(maior > linha):
                criterio_linha += 1
        
        criterio_coluna = 0
        for j in range(lin):
            coluna = 0
            for i in range(col):
                if(i == j):
                    maior = matrizA[i][j]
                else:
                    coluna += matrizA[i][j]
            if(maior > coluna):
                criterio_coluna += 1

        if(criterio_linha != lin and criterio_coluna != col):
            print("Matriz não converge!")
            print(np.matrix(matrizA))
        else:
            vetor_ini = []
            for i in range(lin):
                vetor_ini.append(vetorB[i]/matrizA[i][i])
            iteracao_jacobi(vetor_ini, vetorB, matrizA, count)
            

def iteracao_jacobi(vetorA, vetorB, matriz, count):
    vetor = []
    for i in range(len(matriz[0])):
        sub = 0
        for j in range(len(matriz[0])):
            if(i != j):
                sub -= matriz[i][j]*vetorA[j]
        vetor.append((1/matriz[i][i])*(vetorB[i] + sub))

    valor1 = abs(vetor[0])
    valor2 = abs(vetor[0] - vetorA[0])
    for i in range(len(matriz[0])):
        if(abs(vetor[i]) < valor1):
            valor1 = abs(vetor[i])
        
        if(abs(vetor[i] - vetorA[i]) > valor2):
            valor2 = abs(vetor[i] - vetorA[i])
    
    count = count + 1

    #Iteração
    print('Iteração '+ str(count))
    print('--------------------------------')
    print(np.matrix(vetor))
    print()

    if(round(valor2/valor1, const_aprox()) > const_erro()):
        iteracao_jacobi(vetor, vetorB, matriz, count)


def seidel():
    count = 0

    #Lendo arquivo com a matriz
    nome_arq = "matriz_aumentada.txt"
    arq = open(nome_arq, "r")
    
    #Atribui a Matriz Aumentada a variável matrizA
    matrizA = arquivo_para_matriz(arq.readlines())
    #Cria o vetor vazio B
    vetorB = []

    #Número de linhas da matriz dos cofatores
    lin = len(matrizA)
    
    #Divide a matriz aumentada em duas
    for i in range(lin):
        vetorB.append(matrizA[i][lin])
        matrizA[i].pop(lin)
    
    #Número de colunas da matriz dos cofatores
    col = len(matrizA[0])

    #Verifica se a matriz dos cofatores é quadrada
    if (lin != col):
        print("Matriz [", col, "X", lin, "] não é quadrada")
        print(np.matrix(matrizA))
    else:
        criterio_linha = 0
        for i in range(lin):
            linha = 0
            for j in range(col):
                if(i == j):
                    maior = matrizA[i][j]
                else:
                    linha += matrizA[i][j]
            if(maior > linha):
                criterio_linha += 1
        
        criterio_coluna = 0
        for j in range(lin):
            coluna = 0
            for i in range(col):
                if(i == j):
                    maior = matrizA[i][j]
                else:
                    coluna += matrizA[i][j]
            if(maior > coluna):
                criterio_coluna += 1

        if(criterio_linha != lin and criterio_coluna != col):
            print("Matriz não converge!")
            print(np.matrix(matrizA))
        else:
            vetor_ini = []
            for i in range(lin):
                vetor_ini.append(vetorB[i]/matrizA[i][i])
            iteracao_seidel(vetor_ini, vetorB, matrizA, count)


def iteracao_seidel(vetorA, vetorB, matriz, count):
    vetor = []
    vetorC = vetorA.copy()
    
    for i in range(len(matriz[0])):
        sub = 0
        for j in range(len(matriz[0])):
            if(i != j):
                sub -= matriz[i][j]*vetorC[j]
        vetorC[i] = (1/matriz[i][i])*(vetorB[i] + sub)
        vetor.append(vetorC[i])

    valor1 = abs(vetor[0])
    valor2 = abs(vetor[0] - vetorA[0])
    for i in range(len(matriz[0])):

        if(abs(vetor[i]) > valor1):
            valor1 = abs(vetor[i])
        
        if(abs(vetor[i] - vetorA[i]) > valor2):
            valor2 = abs(vetor[i] - vetorA[i])

    count = count + 1

    #Iteração
    print('Iteração '+ str(count))
    print('--------------------------------')
    print(np.matrix(vetor))
    print()

    if(round(valor2/valor1, const_aprox()) > const_erro()):
        iteracao_seidel(vetor, vetorB, matriz, count)


#METODOS AUXILIARES ======================================================================
def arquivo_para_matriz(arq):
    return [[float(x) for x in line.split()] for line in arq]


def const_aprox():
    return 4


def const_erro():
    return 0.05