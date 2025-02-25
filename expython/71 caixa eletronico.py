valor = int(input('Qual e o valor que o senhor(A) quer sacar? '))
print('--=' * 18)
ciquenta = 0
vinte = 0
dez = 0
um = 0
while True:
    while valor >= 50:
        ciquenta += 1
        valor -= 50
    while valor >= 20:
          vinte += 1
          valor -= 20
    while valor >= 10:
          dez += 1
          valor -= 10
    while valor >= 1:
          um += 1
          valor -= 1
    if valor == 0:
        break
if ciquenta > 0:
    print(f'{ciquenta} notas de R$50')
if vinte > 0:
    print(f'{vinte} notas de R$20')
if dez > 0:
    print(f'{dez} notas de R$10')
if um > 0:
    print(f'{um} notas de R$1')
print('--=' * 18)
