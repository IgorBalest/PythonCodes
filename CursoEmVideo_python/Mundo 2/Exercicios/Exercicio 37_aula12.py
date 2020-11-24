# -*- coding: utf-8 -*-

valor = int(input('Digite um valor: '))
option = int(input('seleciona a base de conversão(1 - binario, 2 - octal, 3 - hexadecimal):'))

if option == 1:     # binario
    valor = bin(valor)
    print('{}'.format(valor))    
    
elif option == 2:   # octal
    valor = oct(valor)
    print('{}'.format(valor))  
    
elif option == 3:   # hexadecimal
    valor = hex(valor)
    print('{}'.format(valor))  
    
    
    
else:
    print('Opção incorreta!!!')