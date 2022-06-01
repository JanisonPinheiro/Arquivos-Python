print('\033[34m-' * 48)
print('Exercício Python #043 - Índice de Massa Corporal')
print('\033[34m-\033[m' * 48)
altura = float(input('Qual sua altura? (m) '))
peso = float(input('Quanto você pesa ? (Kg) '))
imc = peso / (altura * altura)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do Peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
