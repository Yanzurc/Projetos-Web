tupa = []
from random import randint
for c in range(0, 5):
    ale = randint(0, 20)
    tupa += [ale]
print(f'os 5 numeros sorteados foram {tupa}')
print(f'O menor numero sorteado foi {min(tupa)}')
print(f'o maior numero sorteado foi {max(tupa)}')