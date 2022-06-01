
print('\033[34m-' * 42)
print('Exercício Python #038 - Comparando números')
print('\033[34m-\033[m' * 42)
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 == num2:
    print('Não existe valor maior, os dois são iguais.')
elif num1 > num2:
    print('O primeiro valor é maior que o segundo.')
elif num1 < num2:
    print('O segundo valor é maior que o primeiro.')
