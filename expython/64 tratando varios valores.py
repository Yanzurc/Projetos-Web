sabre = 0
cont = 0
print('-=-' * 20)
while sabre != 999:
    sabre = int(input('digite um numero. se quiser parar digite 999: '))
    cont += sabre
print('-=-' * 20)
print('A soma de todos os numeros que você digitou foi {}'.format(cont - 999))