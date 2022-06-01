print('\033[33m=' * 51)
print('\033[36mExercício Python #073 - Tuplas com Times de Futebol ')
print('\033[33m=' * 51)
times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo',
         'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('\033[34m---' * 20)
print(f'Os cinco primeiros colocados foram: \n{times[:5]}')
print('---' * 20)
print('\033[31m---' * 20)
print(f'Os quatro útimos colocados foram \n{times[16:]}')
print('---' * 20)
print('\033[m---' * 20)
print(f'Os times em ordem alfabética \n{sorted(times)}')
print('---' * 20)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}°')
