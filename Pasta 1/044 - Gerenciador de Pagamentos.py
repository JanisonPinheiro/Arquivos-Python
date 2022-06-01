print('\033[34m{:=^80}\033[m'.format(' Exercício Python #044 - Gerenciador de Pagamentos '))
v = float(input('Qual o valor do produto?  R$'))
método1 = v * 10 / 100
método2 = v * 5 / 100
método3 = v
método4 = v * 20 / 100
print('Escolha uma forma de pagamento.')
print('''[ 1 ] À VISTA em dinheiro ou cheque.
[ 2 ] À VISTA no cartão.
[ 3 ] EM ATÉ 2 vezes no cartão.
[ 4 ] 3 vezes ou mais no cartão.''')
escolha = int(input('Ecolha uma das opções: '))
if escolha == 1:
    print('Sua compra de {} vai custar {:.2f} no final. '.format(v, v - método1))
elif escolha == 2:
    print('Sua compra de {}R$ vai custar {:.2f} no final. '.format(v, v - método2))
elif escolha == 3:
    print('Sua compra será parcelada em 2x de {:.2f} SEM JUROS.'.format(v / 2))
    print('Sua compra vai custar {:.2f} no final. '.format(método3))
elif escolha == 4:
    parcela = int(input('Quantas parcelas vão ser? '))
    p = (v + método4) / parcela
    print('Sua commpra será parcelada em {}x de {:.2f} COM JUROS'.format(parcela, p))
    print('Sua compra vai custar {} no final. '.format(v + método4))
else:
    print('Comando INVÁLIDO')
