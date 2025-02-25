num = []
impar = []
par = []
while True:
    a =(int(input('Digite um numero:')))
    num.append(a)
    per = str(input('Você deseja continuar? [S/N]:')).upper()
    if a % 2 == 0:
        par += [a]
    else:
        impar += [a]
    if per == 'N':
        break
print("=-=" * 15)
print(f'os numeros que você digitou {num}')
print(f'os numeros pares que você digitou {par}')
print(f'os numeros impar que você digitou {impar}')
