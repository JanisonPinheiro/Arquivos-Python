print('Exercício Python #084 - Lista composta e análise de dados')
temp = []
principal = []
mai = men = 0
while True:
    temp.append(str(input('NOME: ')))
    temp.append(float(input('PESO: ')))
    if len(principal) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    principal.append(temp[:])
    temp.clear()
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar in 'Nn':
        break
print(f'Total de pessoas cadastrads {len(principal)}.')
print(f'O maior peso foi de {mai}Kg. Peso de', end=' ')
for p in principal:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in principal:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()
