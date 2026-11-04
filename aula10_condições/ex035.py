print('-' * 20)
print('Vamos analisar um triangulo')
print('-' * 20)
r1 = int(input('Primeiro valor da reta 1: '))
r2 = int(input('Segundo valor da reta 2: '))
r3 = int(input('Terceiro valor da reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Os valores podem formar um triangulo')
else:
    print('Os valores não podem formar um triangulo')
