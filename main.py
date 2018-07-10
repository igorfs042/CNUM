#!/usr/bin/python
import zerosDeFuncoes as zf
from decimal import Decimal

#Definindo os intervalos
intervalo_1 = float(input('Intervalo 1: '))
intervalo_2 = float(input('Intervalo 2: '))

#Menu de opções
print('0 - Bissecção')
print('1 - Falsa posição')
print('2 - Ponto fixo')
print('3 - Newton-Raphson')
print('4 - Secante')

#Estrutura relacionando os métodos com as opções do menu
switcher = {
    0: zf.bisseccao,
    1: zf.falsa_posicao,
    2: zf.ponto_fixo,
    3: zf.newton_raphson,
    4: zf.secante
}

#Seleciona qual método será chamado
metodo = switcher.get(int(input('Qual o metodo?')), "nothing")
#Invoca o método escolhido. Independente de qual seja.
raiz = metodo(intervalo_1, intervalo_2)

#Resultado
print('Raíz') 
print('--------------------------------') 
print(raiz)
print()
print('Iterações')
print('--------------------------------') 
print(zf.count)

