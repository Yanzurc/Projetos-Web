print('-=' * 25)
print('               SEQUENCIA BONAFACCI')
print('=-' * 25)
print('')
se = int(input('Quantos termos da sequência Bonafacci você quer ver?: '))
pri = 0
seg = 1
cont = 2
print('')
print('0 → 1 → ', end='')
while cont != se:
    cont += 1
    tres = pri + seg
    pri = seg
    seg = tres
    print(tres, end=' → ')
print('END')