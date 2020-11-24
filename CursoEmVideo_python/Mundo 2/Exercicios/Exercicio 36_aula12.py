# -*- coding: utf-8 -*-


val_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salario: '))
tempo = int(input('Digite em quantos anos pretende pagar: '))

parcela = val_casa / (12 * tempo) 

if parcela >= (0.3 * salario):
    print(' Salario muito pequeno para o financiamento')
else:
    print('Parabens, sua parcela será de {.2} reais.'.format(parcela))
