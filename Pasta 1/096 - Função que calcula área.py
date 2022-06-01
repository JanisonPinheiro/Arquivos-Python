print('Exercício Python #096 - Função que calcula área')


def area(larg, comp):
    a = larg * comp
    print(f'A aréa de um terreno {larg} X {comp} é de {a}')


print('Controle de Terrenos')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
