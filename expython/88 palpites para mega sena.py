from random import randint
jogos = []
num = int(input('Quantos jogos?:'))
jogo = []
for c in range(0, num * 6):
    ale =randint(1, 60)
    jogo.append(ale)
    if len(jogo) == 6:
        jogos.append(jogo[:])
        jogo.clear()
print('='* 37)
print('          JOGOS DA MEGA SENA')
print('=' * 37)
for v in range(0, num):
    print(f'JOGO {v + 1}:{jogos[v]}')
print('='* 37)

    


