import math
import numpy as np

#Definindo minha função. Exemplo: x³ - 9x + 5
def funcao (x):
    func = (x ** 3.0) - (9 * x) + 5
    return func

def trapezio():
    #Definindo os valores iniciais
    somatorio = 0
    operacoes = 0

    #Definindo os intervalos
    intervalo = int(input('Número de Intervalos: '))

    #Definindo os valores de a e b
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))

    h = (b-a)/intervalo

    for i in range(intervalo):
        x0 = a+(h*i)
        x1 = a+(h*(i+1))
        somatorio += funcao(x0) + funcao(x1)
        operacoes += 2
        
    somatorio = somatorio*(h/2)
    operacoes += 3

    print("\nIntegral: " + str(somatorio))
    print('--------------------------------')
    print("Intervalos: " + str(intervalo))
    print('--------------------------------')
    print("h: " + str(h))
    print('--------------------------------')
    print("Operações:" + str(operacoes))
    print('--------------------------------')