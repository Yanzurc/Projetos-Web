lista = []
menor = 99999999999999999999999999999999999999999999999999999999999999999999999999999999
maior = 0
for tiu in range(0, 5):
    cub = (int(input('digite um numero para adcionar a lista:')))
    if cub <= menor:
        lista.insert(0, cub)
        menor = cub
    elif cub >= maior:
        lista.insert(4, cub)
        maior = cub
    else:
        lista.append(cub)
print(lista)