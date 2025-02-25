tupla = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',  'oito', 'nove', 'dez'
while True:
  escolha = int(input('digite um numero entre 0 e 10: '))
  if escolha <= 10 and escolha >= 0:
      break
print(f'tu digiou {tupla[escolha]}')