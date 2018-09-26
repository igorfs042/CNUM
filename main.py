#!/usr/bin/python
import os
import zerosDeFuncoes as zf
import sistemasDeEquacoesLineares as sel
import interpolacaoPolinomial as ip
import minimosQuadrados as mq
import integraisNumericas as num

def sair():
    global cond
    cond = 0

cond = 1

while(cond):
    #Menu de opções
    os.system('cls' if os.name == 'nt' else 'clear')
    print('ZEROS DE FUNÇÕES')
    print('=========================')
    print('1 - Bissecção')
    print('2 - Falsa posição')
    print('3 - Ponto fixo')
    print('4 - Newton-Raphson')
    print('5 - Secante\n')
    print('SISTEMAS DE EQUAÇÕES LINEARES')
    print('=========================')
    print('6 - Eliminação de Gauss')
    print('7 - Fatoração LU')
    print('8 - Gauss - Jacobi')
    print('9 - Gauss - Seidel\n')
    print('INTERPOLAÇÃO POLINOMIAL')
    print('=========================')
    print('10 - Lagrange')
    print('11 - Newton\n')
    print('MÍNIMOS QUADRADOS')
    print('=========================')
    print('12 - Ajuste Linear')
    print('13 - Ajuste Logaritmo')
    print('14 - Ajuste Exponencial')
    print('15 - Ajuste Potencial\n')
    print('INTEGRAIS NUMÉRICAS')
    print('=========================')
    print('16 - Regra dos Trapézios\n')
    print('=========================')
    print('0 - Sair do programa\n')

    #Estrutura relacionando os métodos com as opções do menu
    switcher = {
        0: sair,
        1: zf.bisseccao,
        2: zf.falsa_posicao,
        3: zf.ponto_fixo,
        4: zf.newton_raphson,
        5: zf.secante,
        6: sel.gauss,
        7: sel.lu,
        8: sel.jacobi,
        9: sel.seidel,
        10: ip.lagrange,
        11: ip.newton,
        12: mq.linear,
        13: mq.logaritmo,
        14: mq.exponencial,
        15: mq.potencia,
        16: num.trapezio,
    }

    #Seleciona qual método será chamado
    metodo = switcher.get(int(input('Qual o metodo?')), "nothing")
    #Invoca o método escolhido. Independente de qual seja.
    raiz = metodo()
    input('Pressione ENTER para continuar...')