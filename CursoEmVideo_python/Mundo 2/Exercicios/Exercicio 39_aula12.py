# -*- coding: utf-8 -*

from datetime import date

ano = int(input('Digite o ano do seu nascimento: '))

ano_atual = date.today()
idade = ano_atual.year - ano

if idade  == 18:
    print('ALISTE-SE NO EXERCITO BRASILEIRO, VOCÊ VAI PODER: ANDAR DE MOTO...')
elif idade > 18:
    print('ESTEJA PRESO, FUJÃO!já passou do tempo de se alistar')
else:
    print('Ainda falta {} anos para se alistar :/'.format((ano + 18) - ano_atual.year ))