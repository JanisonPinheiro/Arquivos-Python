print('\033[34m=' * 53)
print('Exercício Python #071 - Simulador de Caixa Eletrônico')
print('=' * 53)
valor = int(input('\033[mQual o Valor a ser sacado? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
