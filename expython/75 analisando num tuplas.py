num = (int(input('numeri digite 1:')),
       int(input('numero digite 2:')),
       int(input('numero digite 3:')),
       int(input('numero digite 4:')))
par = []
print(num)
print(f'os numeros noves foi digitado {num.count(9)} vezes')
if 3 in num:
    print(f'numero 3 posição {num.index(3)+1}')
else:
    print('O numero 3 não foi digitado')
for c in num:
    if c % 2 == 0:
     par += [c]
print(f'os numeros pares digitados foram {par}')