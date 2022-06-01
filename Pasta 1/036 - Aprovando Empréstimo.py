casa = float(input('Qual o valor da casa? R$'))
salário = float(input('Salário do comprador: R$'))
anos = float(input('Quantos anos de finaciamento? '))
mes = anos * 12
mensalidade = salário * 30/100
parcela = casa / mes
print('Para pagar uma casa de {} R$ em {:.0f} anos a prestação será de {:.2f}'.format(casa, anos, parcela))
if parcela > mensalidade:
    print('Seu financiamento foi \033[31mNEGADO\033[m')
    print('O valor da prestação excede os 30% do seu salário')
else:
    print('Seu financiamento foi \033[34m APROVADO\033[m')

