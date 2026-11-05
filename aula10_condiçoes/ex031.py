viagem = float(input('Qual a distancia da sua viagem: '))
if viagem <= 200:
    resultado = viagem * 0.5
    print('O valor da sua viagem ficou em R${:.2f}'.format(resultado))
else:
    resultado = viagem * 0.45
    print('O valor da sua viagem ficou em R${:.2f}'.format(resultado))
