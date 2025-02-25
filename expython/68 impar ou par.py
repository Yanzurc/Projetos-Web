from random import randint
cont = 0
while True:
    esc = str(input('Escolha impar ou par: '))
    print('--=' * 14)
    num = int(input('Escolha um numero: '))
    pc = randint(0, 10)
    total = num + pc
    if esc == 'par':
        if total % 2 == 0:
            print(f' o computador escolheu {pc} e você {num} a soma dos dois e {total} então você GANHOU')
            cont += 1
        else:
            print(f'o computador escolheu {pc} e você {num} a soma dos dois e {total} então você PERDEU')
            break
    if esc == 'impar':
        if total % 2 != 0:
            print(f' o computador escolheu {pc} e você {num} a soma dos dois e {total} então você GANHOU')
            cont += 1
        else:
            print(f'o computador escolheu {pc} e você {num} a soma dos dois e {total} então você PERDEU')
            break
print(f'Você ganhou {cont} vezes')