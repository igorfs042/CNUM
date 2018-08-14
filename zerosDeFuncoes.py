import math
import numpy as np
from decimal import Decimal

#Definindo minha função. Exemplo: x³ - 9x + 5
def funcao (x):
    func = (x ** 3.0) - (9 * x) + 5
    return func
#Definindo a derivada da minha função. Exemplo: 3x² - 9
def dFuncao (x):
    func = (3*x**2) - 9
    return func
#Definindo a função "fi"(x) = x. Exemplo: (x³ + 5)/9
def fFuncao (x):
    func = ((x ** 3) + 5)/9
    return func


#Método da Bissecção
def bisseccao():
    count = 0

    #Definindo os intervalos
    intervalo_1 = float(input('Intervalo 1: '))
    intervalo_2 = float(input('Intervalo 2: '))

    erro = float(input('Erro: '))

    while (abs(intervalo_1 - intervalo_2 ) > erro):
        if (np.sign(funcao((intervalo_1 + intervalo_2)/2)) != np.sign(funcao(intervalo_1))):
            intervalo_2 = (intervalo_1 + intervalo_2)/2
        else:
            intervalo_1 = (intervalo_1 + intervalo_2)/2
        count = count + 1

        raiz = Decimal((intervalo_1 + intervalo_2)/2)

        #Iteração
        print('Iteração '+ str(count))
        print('--------------------------------') 
        print(raiz)
        print()


#Método da Falsa Posição
def falsa_posicao():
    count = 0

    #Definindo os intervalos
    intervalo_1 = float(input('Intervalo 1: '))
    intervalo_2 = float(input('Intervalo 2: '))

    erro = float(input('Erro: '))

    intervalo_novo = ((intervalo_1*funcao(intervalo_2)) - (intervalo_2*funcao(intervalo_1)))/(funcao(intervalo_2) - funcao(intervalo_1))
    while (abs(funcao(intervalo_novo)) > erro):
        if (np.sign(funcao(intervalo_1)*funcao(intervalo_novo)) > 0):
            intervalo_1 = intervalo_novo
        else:
            intervalo_2 = intervalo_novo
        intervalo_novo = ((intervalo_1*funcao(intervalo_2)) - (intervalo_2*funcao(intervalo_1)))/(funcao(intervalo_2) - funcao(intervalo_1))
        count = count + 1

        raiz = Decimal(intervalo_novo)

        #Iteração
        print('Iteração '+ str(count))
        print('--------------------------------') 
        print(raiz)
        print()


#Método do Ponto Fixo
def ponto_fixo():
    count = 0

    #Definindo os intervalos
    intervalo_1 = float(input('Intervalo 1: '))
    intervalo_2 = float(input('Intervalo 2: '))

    erro = float(input('Erro: '))

    intervalo_novo = fFuncao((intervalo_1 + intervalo_2)/2)
    while (abs(funcao(intervalo_novo)) > erro):
        intervalo_novo = fFuncao(intervalo_novo)
        count = count + 1

        raiz = Decimal(intervalo_novo)

        #Iteração
        print('Iteração '+ str(count))
        print('--------------------------------') 
        print(raiz)
        print()


#Método de Newton-Raphson
def newton_raphson():
    count = 0

    #Definindo os intervalos
    intervalo_1 = float(input('Intervalo 1: '))
    intervalo_2 = float(input('Intervalo 2: '))

    erro = float(input('Erro: '))

    while (abs(funcao(intervalo_2)) > erro):
        intervalo_2 = intervalo_2 - funcao(intervalo_2)/dFuncao(intervalo_2)
        count = count + 1

        raiz = Decimal(intervalo_2)

        #Iteração
        print('Iteração '+ str(count))
        print('--------------------------------') 
        print(raiz)
        print()


#Método da Secante
def secante():
    count = 0

    #Definindo os intervalos
    intervalo_1 = float(input('Intervalo 1: '))
    intervalo_2 = float(input('Intervalo 2: '))
    intervalo_novo = (intervalo_2 - (((intervalo_1 - intervalo_2) / (funcao(intervalo_1) - funcao(intervalo_2))) * funcao(intervalo_2)))

    erro = float(input('Erro: '))
    
    while (1):
        intervalo_1 = intervalo_2
        intervalo_2 = intervalo_novo

        intervalo_novo = (intervalo_2 - (((intervalo_1 - intervalo_2) / (funcao(intervalo_1) - funcao(intervalo_2))) * funcao(intervalo_2)))

        erro_iteracao = abs((intervalo_novo - intervalo_2) / intervalo_novo)

        count = count + 1

        raiz = Decimal(intervalo_novo)

        #Iteração
        print('Iteração '+ str(count))
        print('--------------------------------') 
        print(raiz)
        print()

        if (erro_iteracao < erro):
            break