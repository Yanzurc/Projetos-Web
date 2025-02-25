media = 0
R = ''
soma = 0
mn = []
while R != 'N':
    print('--=--' * 10)
    media += 1
    num = int(input(' digite o {}° numero: '.format(media)))
    soma += num
    mn += [num]
    R = str(input(' Você deseja continuar [S/N]:')).upper()
    print('--=--' * 10)
    print('')
print('=-=' * 15)
print('Você digite numeros {} vezes\nA media dos numeros que você digitou foi {}\nO menor numero digitado foi {}\nO maior numero digitado foi {}'.format(media, soma / media, max(mn), min(mn)))
print('=-=' * 15)
