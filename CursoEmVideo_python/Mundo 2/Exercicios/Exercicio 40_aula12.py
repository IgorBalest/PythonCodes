# -*- coding: utf-8 -*-

'''
Crie um programa que leia duas notas de um aluno e calcule sua 
média. mostrando uma mensagem no final, de acordo com a média atingida:

-média abaixo de 5.0:
    REPROVADO!

-média entre 5.0 e 6.9:
    RECUPERAçÂO!
    
-média 7.0 ou superior:
    APROVADO!

'''


nota_a = float(input('Digite a primeira nota: '))
nota_b = float(input('Digite a segunda nota: '))

media = (nota_a + nota_b) / 2

if media >= 7.0:
    print('APROVADO!!')
    
elif media >= 5.0 and media <= 6.9:
    print('Recuperação')
elif media < 5.0:
    print('REPROVADO!!!')
    
    
    