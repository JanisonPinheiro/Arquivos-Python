print('\033[34m-' * 43)
print('Exercício Python #039 - Alistamento Militar')
print('\033[34m-\033[m' * 43)
from datetime import date
print('''Qual  o seu sexo?
[ 1 ] FEMININO
[ 2 ] MASCULINO''')
sexo = int(input('Escolha uma opção: '))
if sexo == 1:
    print('Você não precisa se alistar. ')
elif sexo == 2:
    atual = date.today().year
    ano = int((input('Ano do seu nascimento: ')))
    idade = atual - ano
    print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
    if idade == 18:
        print('Hora de se alistar.')
    elif idade > 18:
        print('Passou da hora de se alistar')
    elif idade < 18:
        saldo = 18 - idade
        if saldo == 1:
            print('Você ainda não tem 18 anos. Falta {} ano para o seu alistamento.'.format(saldo))
        else:
            print('Você ainda não tem 18 anos. Faltam {} anos para o seu alistamento.'.format(saldo))
else:
    print('Tu é cego que não tá vendo que não tem essa opção?')