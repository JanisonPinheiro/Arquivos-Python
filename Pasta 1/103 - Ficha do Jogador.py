print('Exercício Python #103 - Ficha do Jogador')


def ficha(jog='<desconhcido>', gols=0):
    print(f'O jogador {jog} fez {gols} gol (s) no campeonato. ')


n = str(input('Nome do Jogador: '))
g = str(input('Números de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
