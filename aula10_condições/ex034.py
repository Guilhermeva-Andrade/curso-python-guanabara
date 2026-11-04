salario = float(input('Qual o seu salario: '))
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print('Seu novo salario é R${:.2f}'.format(aumento))
