print('\033[34m=' * 49)
print('Exercício Python #069 - Análise de dados do grupo')
print('=' * 49)
total = mas = fem = idademaisde = mulhercommenosdevinte = 0
while True:
    print('\033[m-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('IDADE: '))
    if idade >= 18:
        idademaisde += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F] ')).strip().upper()[0]
        total += 1
        if sexo in 'M':
            mas += 1
        elif sexo in 'F':
            fem += 1
            if idade < 20:
                mulhercommenosdevinte += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break
print(f' {mas} pessoas são do sexos masculino '
      f'\n {fem} pessoas são do sexos feminino'
      f'\n Termos {idademaisde} pessoas maior de 18 anos'
      f'\n Mulheres com menos de vinte anos {mulhercommenosdevinte}')
