casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salario do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação da casa será de R${:.2f}'.format(prestacao))
print('comprando tem que pagar R${:.2f} e mínimo é de R${:.2f}'.format(prestacao, minimo))
if prestacao <= minimo:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo reprovado!')
