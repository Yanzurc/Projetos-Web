num = []
true = 0
while True:
    true = (int(input('Digite um valor: ')))
    if true in num:
        print('O numero ja foi digite, não adicionado.')
    else:
     print('Numero adicionado...')
     num.append(true)
    per = (input('Você deseja continuar? [S/N]: ')).upper()
    print('=-=' * 17)
    if per == 'N':
        break
print(f'Os numeros digitados foram {num}')
