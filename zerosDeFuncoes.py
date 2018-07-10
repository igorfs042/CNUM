import math
import numpy as np
from decimal import Decimal

#Definindo minha função. Exemplo: x³ - 9x + 5
def funcao (x):
    return ((x ** 3.0) - (9 * x) + 5)
#Definindo a derivada da minha função. Exemplo: 3x² - 9
def dFuncao (x):
    return ((3*x**2) - 9)
#Definindo a função "fi"(x) = x. Exemplo: (x³ + 5)/9
def fFuncao (x):
    return ((x ** 3) + 5)/9
#Definindo o erro. Exemplo: 10²
erro = Decimal('0.01')
#Contador de iterações
count = 0

#Método da Bissecção
def bisseccao(intervalo_1, intervalo_2):
    global count

    while (abs(intervalo_1 - intervalo_2 ) > erro):
        if (np.sign(funcao((intervalo_1 + intervalo_2)/2)) != np.sign(funcao(intervalo_1))):
            intervalo_2 = (intervalo_1 + intervalo_2)/2
        else:
            intervalo_1 = (intervalo_1 + intervalo_2)/2
        count = count + 1
    return Decimal((intervalo_1 + intervalo_1)/2)

#Método da Falsa Posição
def falsa_posicao(intervalo_1, intervalo_2):
    global count

    intervalo_novo = ((intervalo_1*funcao(intervalo_2)) - (intervalo_2*funcao(intervalo_1)))/(funcao(intervalo_2) - funcao(intervalo_1))
    while (abs(funcao(intervalo_novo)) > erro):
        if (np.sign(funcao(intervalo_1)*funcao(intervalo_novo)) > 0):
            intervalo_1 = intervalo_novo
        else:
            intervalo_2 = intervalo_novo
        intervalo_novo = ((intervalo_1*funcao(intervalo_2)) - (intervalo_2*funcao(intervalo_1)))/(funcao(intervalo_2) - funcao(intervalo_1))
        count = count + 1
    return Decimal(intervalo_novo)

#Método do Ponto Fixo
def ponto_fixo(intervalo_1, intervalo_2):
    global count

    intervalo_novo = fFuncao((intervalo_1 + intervalo_2)/2)
    while (abs(funcao(intervalo_novo)) > erro):
        intervalo_novo = fFuncao(intervalo_novo)
        count = count + 1
    return Decimal(intervalo_novo)

#Método de Newton-Raphson
def newton_raphson(intervalo_1, intervalo_2):
    global count

    while (abs(funcao(intervalo_2)) > erro):
        intervalo_2 = intervalo_2 - funcao(intervalo_2)/dFuncao(intervalo_2)
        count = count + 1
    return Decimal(intervalo_2)

#Método da Secante
def secante(intervalo_1, intervalo_2):
    global count
    intervalo_novo = (intervalo_2 - (((intervalo_1 - intervalo_2) / (funcao(intervalo_1) - funcao(intervalo_2))) * funcao(intervalo_2)))
    
    while (1):
        intervalo_1 = intervalo_2
        intervalo_2 = intervalo_novo

        intervalo_novo = (intervalo_2 - (((intervalo_1 - intervalo_2) / (funcao(intervalo_1) - funcao(intervalo_2))) * funcao(intervalo_2)))

        erro_iteracao = abs((intervalo_novo - intervalo_2) / intervalo_novo)

        count = count + 1

        if (erro_iteracao < erro):
            return intervalo_novo