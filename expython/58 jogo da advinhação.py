from time import sleep
from random import randint
pc = randint(1, 10)
eu = 0
while pc != eu:
    print('=-=' * 21)
    eu = int(input('qual e o numero que o pc escolheu?(numeros entre 1 e 10): '))
    print('=-=' * 21)
    print('')
    if eu != pc:
        print('Você errou!, não tem problema você pode tentar de novo')
        sleep(2)

print('parabens voce acertou!!!')