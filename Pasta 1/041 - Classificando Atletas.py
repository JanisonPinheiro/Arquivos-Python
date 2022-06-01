print('\033[34m-' * 45)
print('Python Exercício #041 - Classificando Atletas')
print('\033[34m-\033[m' * 45)
ano = int(input('Ano de Nascimento: '))
from datetime import date
ano_atual = date.today().year
idade = ano_atual - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classifição: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
