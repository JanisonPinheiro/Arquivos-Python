print('\033[34m=' * 45)
print('Exercício Python #065 - Maior e Menor valores')
print('=' * 45)
res = 'Ss'
soma = quant = media = maior = menor = 0
while res in 'Ss':
        num = int(input('\033[mDigite um número: '))
        soma += num
        quant += 1
        if quant == 1:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
        res = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
