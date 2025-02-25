while True:
 mul = 0
 num = int(input('Qual tabuada você quer ver?: ', ))
 if num < 0:
    break
 print('')
 print(f'Tabuada do {num }')
 print('=' * 14)
 while mul < 10:
    mul += 1

    print(f'{num} X {mul} = {num * mul}')
 print('=' * 14)
