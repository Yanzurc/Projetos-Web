lista = []
while True:
    lista.append(int(input('Digite um valor:')))
    per = str(input('Você deseja continuar? [S/N]:')).upper()
    if per == 'N':
        break
lista.sort(reverse=True)
print(lista)
print(len(lista))
if 5 in lista:
    print('O 5 foi digitado')
else:
    print('O 5 não foi digitado')