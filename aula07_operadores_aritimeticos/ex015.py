km = float(input('Qual a quantidade de km percorrido: '))
dias = int(input('Quantos dias você alugou o carro? '))
valor = dias * 60 + km * 0.15
print('O total a pagar é de R${:.2f}'.format(valor))
