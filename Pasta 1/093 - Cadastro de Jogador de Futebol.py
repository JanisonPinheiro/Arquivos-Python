print('Exercício Python #093 - Cadastro de Jogador de Futebol')
partidas = list()
dicio = dict()
dicio['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {dicio["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gol na partida {c + 1}°? ')))
dicio['gols'] = partidas[:]
dicio['total'] = sum(partidas)
print('\033[34m-=' * 30)
print(dicio)
print('\033[34m-=\033[m' * 30)
for k, v in dicio.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dicio["nome"]} jogou {len(dicio["gols"])} partidas')
for i, v in enumerate(dicio['gols']):
    print(f'    => Na partida {i + 1}, fez {v} gols. ')
print(f'Foi um total de {dicio["total"]} gols ')

