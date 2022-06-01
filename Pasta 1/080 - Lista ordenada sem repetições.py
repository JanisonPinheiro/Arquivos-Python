print('Exercício Python #080 - Lista ordenada sem repetições')
lista = []
maior = 0
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0:
        lista.append(num)
        maior = num
        print('Adicionado ao final da lista...')
    else:
        posmaior = 0
        for n in lista:
            if num > n:
                maior = num
                posmaior = lista.index(n) + 1
        lista.insert(posmaior, num)
        if lista.index(num) == (len(lista) -1):
            print('Adicionado ao final da lista...')
        else:
            print(f'Adicionado na posição {lista.index(num)} da lista...')
print('-=' * 30)
print(lista)
