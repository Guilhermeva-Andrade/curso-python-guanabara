carro = float(input('Qual a velocidade do carro? '))
if carro > 80:
    print('Voce foi multado em R${:.2f} por exceder o limite de 80Km/h'.format((carro - 80) * 7))
else:
    print('Você esta dentro da velocidade')
print('Tenha um bom dia! Dirija com segurança')
