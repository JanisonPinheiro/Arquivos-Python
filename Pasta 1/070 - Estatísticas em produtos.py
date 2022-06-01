print('\033[34m=' * 48)
print('Exercício Python #070 - Estatísticas em produtos')
print('=' * 48)
tot = totmil = barato = cont = probarato = 0
while True:
    print('\033[m-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    pro = str(input('Nome do Produto: ')).strip().upper()
    pre = float(input('Preço: R$'))
    tot += pre
    cont += 1
    if pre > 1000:
        totmil += 1
    if cont == 1:
        barato = pre
        probarato = pro
    else:
        if pre < barato:
            barato = pre
            probarato = pro
    con = ' '
    print('-' * 20)
    while con not in 'SN':
        con = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if con == 'N':
        break
print(f'O total da compra foi R$ {tot:.2f}'
      f'\nTemos {totmil} custando mais de R$1000.00'
      f'\nO produto  mais barato foi {probarato} custa {barato:.2f} ')
