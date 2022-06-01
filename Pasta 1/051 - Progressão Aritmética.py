print('=' * 45)
print('Exercício Python #051 - Progressão Aritmética')
print('=' * 45)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Segundo termo: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(c, end='-> ')
print('Acabou')
