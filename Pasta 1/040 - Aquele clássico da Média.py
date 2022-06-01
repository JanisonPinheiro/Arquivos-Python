print('\033[34m-' * 48)
print('Exercício Python #040 - Aquele clássico da Média')
print('\033[34m-\033[m' * 48)
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f} a média é {:.1f}'.format(n1, n2, media))
if media < 5:
    print('REPROVADO')
elif 7 > media >= 5:
    print('RECUPERÇÃO')
elif media > 6:
    print('APROVADO')
