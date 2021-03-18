# -*- coding: utf-8 -*-
"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
de zero a vinte.

seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

"""
elem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')

n = 1


if n > 0 and n < 20:    
    n = int(input('Digite um número: '))
    print(f'Você digitou o número {elem[n]}')
else:
    print('Número inválido')
    