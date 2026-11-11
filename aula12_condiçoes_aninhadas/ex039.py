from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print('Quem nascem em {} tem {} de idade em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar este ano!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} de anos para o seu alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamato será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado')
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
