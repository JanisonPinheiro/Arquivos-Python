print('Exercício Python #090 - Dicionário em Python')
dici = dict()
dici['nome'] = str(input('Nome: '))
dici['media'] = float(input('Média: '))
print(f'O nome é igual a {dici["nome"]}')
print(f'Média igual a {dici["media"]}')
if dici['media'] >= 7:
    dici['situação'] = 'Aprovado'
else:
    dici['situação'] = 'Reprovado'
print(f'A situação é igual a {dici["situação"]}')
print('-' * 12)
for k, v in dici.items(): #outra maneira de fazer
    print(f'-{k} é igual a {v}')



