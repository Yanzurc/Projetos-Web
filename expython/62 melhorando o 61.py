prima = int(input('digite o primeiro termo: '))
razao = int(input('digite a razão: '))
dez = 0
pri = prima
todos = 0
v = 10
while v != 0:
    todos += v
    while dez != todos:
          print('-> {}'.format(pri), end=' ')
          dez += 1
          pri += razao
    print('')
    v = int(input('Você quer ver quantos termos a mais?: '))
print('finished')