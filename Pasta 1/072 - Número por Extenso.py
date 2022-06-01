print('\033[34m°' * 42)
print('Exercício Python #072 - Número por Extenso')
print('°' * 42)
lista = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
         'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
         'Dez', 'Onze', 'Doze', 'Treze', 'Quartoze',
         'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
         'Dezoneve', 'Vinte')
while True:
    num = int(input('\033[mDigite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
print(f'Você digitou o número {lista[num]}')
