print('\033[34m=' * 54)
print('Exercício Python #078 - Maior e Menor valores na Lista')
print('=' * 54)
listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'\033[mDigite o valor para a posição {c}: ')))
print('-=' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {max(listanum)} nas posições {listanum.index(max(listanum))} ')
print(f'O menor valor digitado foi {min(listanum)} nas posições {listanum.index(min(listanum))}')
