num = []
pos = 0
u = 0
y = 0
bb = 99999999999999999999999999999999999999999999999999999999999999999999
for tick in range(0, 5):
    num.append(int(input(f'digite um numero para a posição {tick}: ')))
    for w, v in enumerate(num):
        if u <= v:
            u = v
            pos = w
        if v <= bb:
            bb = v
            y = w
print('')
print(f'Você digitou os numeros {num}')
print(f'O maior numero digitado foi {max(num)} e a posição do numero foi {pos}\nO menor numero digitado foi {min(num)} e a posição do numero foi {y}')