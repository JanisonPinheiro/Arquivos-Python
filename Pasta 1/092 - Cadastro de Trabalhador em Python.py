print('Exercício Python #092 - Cadastro de Trabalhador em Python')
from datetime import datetime
trab = dict()
trab['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimeno: '))
trab['idade'] = datetime.now().year - ano
trab['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if trab['ctps'] != 0:
    trab['contratação'] = int(input('Ano de contratação: '))
    trab['Salário'] = float(input('Salário: R$ '))
    trab['aposentadoria'] = trab['idade'] + (trab['contratação'] + 35) - datetime.now().year
    print()
    print(trab)
    for k, v in trab.items():
        print(f'- {k} tem o valor {v}')


