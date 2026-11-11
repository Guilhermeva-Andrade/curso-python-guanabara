nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = nota1 + nota2 / 2
if 7 > media >= 5:
    print('O aluno precisa de recuperçaão')
elif media < 5:
    print('O aluno foi reprovado')
elif media >= 7:
    print('O aluno foi aprovado')
