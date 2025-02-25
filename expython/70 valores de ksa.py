totale = 0
mil = 0
barato = 2000000000000000
red = ''
while True:
    nombre = str(input('Qual e o nome do movel que você quer?:'))
    preço = float(input('Qual e o preço?:'))
    escolha = str(input('voce deseja continuar a colocar novos protudos? [S/N]: ')).upper()
    totale += preço
    if preço >= 1000:
        mil += 1
    if preço < barato:
        barato = preço
        red = nombre
    if escolha == 'N':
        break
print('-==' * 13)
print(f'o total de tudo foi de R${totale}\nA quantidade de produtos que custam mais de R$1000 são {mil}\nO produto mais barato foi o {red} custando R${barato}')
