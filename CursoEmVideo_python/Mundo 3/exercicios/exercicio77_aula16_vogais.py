# -*- coding: utf-8 -*-
"""
crie um programa que tenha uma tupla com várias palavras( não usar acentos). Depois disso.
você deve mostrar, para cada palavra, quais são as suas vogais.

"""

palavras = ('dicionario', 'abobado', 'putrefato', 'pai')

print(len(palavras))
print(len(palavras[0]))

i = j = 0

for i in range(0 , len(palavras)):          # percorre os elementos da tupla
    print(f'na palavra {palavras[i]} temos as vogais:')
    for j in range(0, len(palavras[i])):    #percorre as letras do elemento
        letra = palavras[i][j] 
        if letra == 'a' or letra == 'e' or letra == 'i' or letra =='o' or letra=='u':
            print(palavras[i][j], end=' - ')
    print('\n')
    

        