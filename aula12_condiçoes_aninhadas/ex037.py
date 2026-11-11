num = int(input('Digite um número inteiro'))
print('''Escolha uma das bases para conversão:
[ 1 ] converta em Binário
[ 2 ] converta em Octal
[ 3 ] converta em Hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido em binário é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido em octal é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido em hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida!')
    