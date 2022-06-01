print('Exercício Python #095 - Aprimorando os Dicionários')
time = list()
partidas = list()
dicio = dict()
while True:
    dicio.clear()
    dicio['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {dicio["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gol na partida {c + 1}? ')))
    dicio['gols'] = partidas[:]
    dicio['total'] = sum(partidas)
    time.append(dicio.copy())
    while True:
        resp = str(input('Quer cntinuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
print('cod', end=' ')
for i in dicio.keys():
    print(f'{i:<15}', end=' ')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar os dads de qual jogador? (999 ENCERRA) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:' )
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols ')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')