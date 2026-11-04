a = int(input('Qual o primeiro numero: '))
b = int(input('Qual o segundo numero: '))
c = int(input('Qual o terceiro numero: '))
menor = a
if a < b and a < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor numero digitado foi {}'.format(menor))
print('O maior numero digitado foi {}'.format(maior))
